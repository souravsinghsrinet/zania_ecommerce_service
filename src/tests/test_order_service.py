import pytest
from sqlalchemy.orm import Session
from src.app.services.order_service import OrderService
from src.app.models.product import Product
from src.app.schemas.order import OrderCreate, OrderItemCreate
from unittest.mock import MagicMock


@pytest.fixture
def mock_db():
    return MagicMock(spec=Session)


def test_create_an_order(mock_db):
    # Arrange: Setup mock product with stock
    product = Product(id=1, name="Laptop", description="Gaming Laptop", price=1000, stock=10)
    mock_db.query().filter().first.return_value = product

    # Mock commit and refresh to avoid real DB operations
    mock_db.commit.return_value = None
    mock_db.refresh.return_value = None
    mock_db.add.return_value = None

    # Prepare order data
    order_data = OrderCreate(items=[OrderItemCreate(product_id=1, quantity=2)])

    # Act: Call the service method
    order_service = OrderService(mock_db)
    result = order_service.create_an_order(order_data)

    # Assert: Validate the expected behavior
    assert result.total_price == 2000
    assert len(result.products) == 1
    assert result.products[0].product_id == 1
    assert result.products[0].quantity == 2
    mock_db.commit.assert_called_once()
