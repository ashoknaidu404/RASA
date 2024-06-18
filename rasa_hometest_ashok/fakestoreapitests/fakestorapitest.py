import pytest
from requests.exceptions import RequestException
import fakestoreapi


@pytest.fixture
def setup_cart():
    # Check if the system is online

    try:
        response = fakestoreapi.get_request("")
        if response.status_code == 200:
            print("System is online. Setting up cart...")
        else:
            pytest.skip("System is offline. Skipping tests.")
    except RequestException as e:
        pytest.skip(f"Failed to connect to system: {e}")


def test_get_all_certs(setup_cart):
    response = fakestoreapi.get_request("carts")
    print(response.json())
    assert response.status_code == 200
    carts = response.json()
    assert isinstance(carts, list)
    assert any(cart["id"] == 7 for cart in carts)


def test_get_single_certs(setup_cart):
    response = fakestoreapi.get_request("carts/" + "5")
    print(response.json())
    assert response.status_code == 200
    carts = response.json()
    assert carts["id"] == 5


def test_get_limit_results(setup_cart):
    response = fakestoreapi.get_request("carts?limit=" + "5")
    print(response.json())
    assert response.status_code == 200
    carts = response.json()
    assert isinstance(carts, list)
    expected_ids = [1, 2, 3, 4, 5]
    for expected_id in expected_ids:
        assert any(cart["id"] == expected_id for cart in carts), f"ID {expected_id} not found in carts"


def test_update_cart(setup_cart):
    cart_id = 7
    endpoint = f"carts/{cart_id}"
    payload = {
        "userId": 3,
        "date": "2019-12-10",
        "products": [{"productId": 1, "quantity": 3}]
    }

    response = fakestoreapi.put_request(endpoint, payload)
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    response_json = response.json()
    assert response_json["id"] == cart_id, f"Expected cart ID {cart_id} but got {response_json['id']}"
    assert response_json["userId"] == payload[
        "userId"], f"Expected user ID {payload['userId']} but got {response_json['userId']}"


def test_add_cart_entry():
    payload = {
        "userId": 8,
        "date": "2020-06-18",
        "products": [{"productId": 18, "quantity": 1}]
    }

    response = fakestoreapi.post_request("carts", payload)
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    response_json = response.json()
    assert response_json.get("id") is not None, "Expected cart ID in response but none found"
    assert response_json["userId"] == payload[
        "userId"], f"Expected user ID {payload['userId']} but got {response_json['userId']}"


def test_view_cart_contents(setup_cart):
    response = fakestoreapi.get_request("carts")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_remove_product_from_cart(setup_cart):
    user_id = 8
    url = f"users/{user_id}"
    response = fakestoreapi.delete_request(url)
    assert response.status_code == 200
