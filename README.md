# zania_ecommerce_service
This is an assignment project from Zania.ai. Requirement is to build an small e-commerce backend with endpoint to get products, add products and place orders.

## Overview

This is a production-grade RESTful API for a simple e-commerce platform built with FastAPI. The API allows users to view available products, add new products, and place orders. It includes features like:

* Stock management

* Order validation

* Exception handling

* Unit and integration testing

* Dockerized deployment

## Prerequisites

Ensure you have the following installed before running the project:

* Python 3.9+

* pip (Python package manager)

* Docker (if running in a container)

* PostgreSQL (or SQLite for local development)

## Installation & Setup

1. Clone the Repository

```bash
git clone https://github.com/souravsinghsrinet/zania_ecommerce_service.git
cd zania_ecommerce_service
```

2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Configure Environment Variables

Create a app.env file in the root directory and specify your database connection details:

```bash
DB_URL=sqlite:///./test.db  # Use PostgreSQL for production
```

5. Initialize the Database

```bash
python -m src.app.db
```

## Running the Application

* Run Locally

```bash
uvicorn main:app --reload
```
The API will be available at http://127.0.0.1:8000

* Run with Docker
Take advantage of available Makefile
  * To build a docker container
  ```bash
  make build
  ```
  * To run a docker image
  ```bash
  make run
  ```
  * To remove a docker container
  ```bash
  make remove
  ```
  * To run all the above together
  ```bash
  make rebuild
  ```

## API Endpoints

* Products

```bash
GET /v1/products → Retrieve all available products

POST /v1/products → Add a new product
```

* Orders
```bash
POST /orders → Place an order
```

## Testing

Run the unit and integration tests using pytest:
```bash
pytest -v
```

## Project Structure
```bash
├── src
│   ├── app
│   │   ├── models                    # Database models (Product, Order)
│   │   │   ├── order.py
│   │   │   ├── product.py
│   │   ├── routes                    # API Endpoints
│   │   │   ├── v1
│   │   │   │   ├── orders.py
│   │   │   │   ├── products.py
│   │   ├── schemas                   # Pydantic schemas for request/response validation
│   │   │   ├── order.py
│   │   │   ├── product.py
│   │   ├── services                  # Business logic services
│   │   │   ├── order_service.py
│   │   │   ├── product_service.py
│   │   ├── utils                     # Common utility methods such as Database connection setup
│   │   │   ├── db.py
│   │   ├── main.py         # FastAPI application entry point
│   ├── tests
│   │   ├──test_app.py      # Integration test script
│   │   ├──test_order_service.py                 # Unit test script
│   ├── run.py              # App runner via uvicorn
├── Dockerfile              # Docker setup
├── Makefile                # Automate docker script
├── requirements.txt        # Python dependencies
├── README.md               # Documentation
```
