from fastapi.testclient import TestClient
from src.app.main import app
from src.app.utils.db import init_db, SessionLocal
from src.app.models.product import Product

client = TestClient(app=app)


def setup_module():
    init_db()


def add_test_products():
    db = SessionLocal()
    db.add(Product(name="Garmin Runner 255", description="A Garmin watch for athletes", price=40000, stock=20))
    db.commit()
    db.close()


def test_get_products():
    add_test_products()
    response = client.get("/v1/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_add_product():
    product_data = {
        "name": "Smartphone",
        "description": "A high-end smartphone",
        "price": 69999.99,
        "stock": 20
    }
    response = client.post("/v1/products", json=product_data)
    assert response.status_code == 201
    response_json = response.json()
    assert "status" in response_json
    assert "data" in response_json
    response_data = response_json["data"]
    assert response_data["name"] == product_data["name"]
    assert response_data["description"] == product_data["description"]
    assert response_data["price"] == product_data["price"]
    assert response_data["stock"] == product_data["stock"]


def test_add_product_input_validation():
    product_data = {
        "name": "Mac book Pro",
        "description": "An apple laptop",
        "price": 230000,
        "stock": -1
    }
    response = client.post("/v1/products", json=product_data)
    assert response.status_code == 422


def test_place_order_input_validation():
    order_item = {
        "items": [
            {
                "product_id": 11,   # this id doesn't exits
                "quantity": 3
            }
        ]
    }
    response = client.post("/v1/orders", json=order_item)
    assert response.status_code == 400


def test_place_order():
    order_item = {
        "items": [
            {
                "product_id": 1,
                "quantity": 3
            },
            {
                "product_id": 2,
                "quantity": 5
            }
        ]
    }
    product_price_map = {
        1: 40000,
        2: 69999.99
    }

    response = client.post("/v1/orders", json=order_item)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["status"] == "completed"
    expected_price = 0
    for each_item in order_item.get("items", []):
        expected_price += (each_item["quantity"] * product_price_map[each_item["product_id"]])
    assert expected_price == response_data["total_price"]

