import pytest
from fastapi.testclient import TestClient
from noodle.main import app


@pytest.fixture(scope="session")
def client():
    return TestClient(app)


@pytest.fixture(scope="function")
def order_payload():
    return {
        "mode": 0,
        "flavor": "beef",
        "toppings": ["onions", "spice"]
    }


@pytest.fixture(scope="function")
def game_payload():
    return {
        "mode": 1,
        "flavor": "beef"
    }