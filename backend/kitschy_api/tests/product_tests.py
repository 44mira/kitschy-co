import pytest
from model_bakery import baker

"""
NOTE: Negative values in stock represent pre-orders
Tests:
1. TestProductAPI - CRUD operations
2. TestProductPreOrderAPI - Pre-order operations
3. TestInvalidProductAPI - Invalid data
4. Edge Cases - Empty data
"""


# Tests basic CRUD
@pytest.mark.django_db
class TestProductAPI:

    endpoint = "/api/products/"

    def test_get_all_products(self, api_client):
        """GET api/products/ - get all products"""

        baker.make(
            "Product", _quantity=10
        )  # Creates 10 instances of Product, each with random data
        response = api_client.get("/api/products/")

        assert response.status_code == 200
        assert len(response.data) == 10

    def test_get_single_product(self, api_client):
        product = baker.make("Product")
        response = api_client.get(f"/api/products/{product.product_id}/")

        assert response.status_code == 200
        assert response.data["product_id"] == str(product.product_id)

    def test_create_product(self, authenticated_user):
        product = {
            "name": "Test Product",
            "desc": "Test Description",
            "price": 10.00,
            "stock": 10,
        }
        response = authenticated_user.post("/api/products/", product)

        assert response.status_code == 201
        assert response.data["name"] == product["name"]

    def test_update_product(self, authenticated_user):
        product = baker.make("Product")
        response = authenticated_user.put(
            f"/api/products/{product.product_id}/",
            {
                "name": "Updated Product",
                "desc": "Updated Description",
                "price": 20.00,
                "stock": 20,
            },
        )

        assert response.status_code == 200

    def test_delete_product(self, authenticated_user):
        product = baker.make("Product")
        response = authenticated_user.delete(
            f"/api/products/{product.product_id}/"
        )

        assert response.status_code == 204
        assert not response.data


# Tests for pre-orders
@pytest.mark.django_db
class TestProductPreOrderAPI:

    endpoint = "/api/products/"

    def test_pre_order_product(self, authenticated_user):
        product = {
            "name": "Pre-Order Product",
            "desc": "Pre-Order Description",
            "price": 30.00,
            "stock": -10,
        }
        response = authenticated_user.post("/api/products/", product)

        assert response.status_code == 201
        assert response.data["name"] == product["name"]

    def test_update_pre_order_product(self, authenticated_user):
        product = baker.make("Product", stock=-10)
        response = authenticated_user.put(
            f"/api/products/{product.product_id}/",
            {
                "name": "Updated Pre-Order Product",
                "desc": "Updated Pre-Order Description",
                "price": 40.00,
                "stock": -20,
            },
        )

        assert response.status_code == 200

    def test_delete_pre_order_product(self, authenticated_user):
        product = baker.make("Product", stock=-10)
        response = authenticated_user.delete(
            f"/api/products/{product.product_id}/"
        )

        assert response.status_code == 204
        assert not response.data


# Tests for invalid data
@pytest.mark.django_db
class TestInvalidProductAPI:

    endpoint = "/api/products/"

    def test_create_invalid_product(self, authenticated_user):
        product = {
            "name": "Invalid Product",
            "desc": "Invalid Description",
            "price": -10.00,
            "stock": 10,
        }
        response = authenticated_user.post("/api/products/", product)

        assert response.status_code == 400

    def test_update_invalid_product(self, authenticated_user):
        product = baker.make("Product")
        response = authenticated_user.put(
            f"/api/products/{product.product_id}/",
            {
                "name": "Updated Invalid Product",
                "desc": "Updated Invalid Description",
                "price": -20.00,
                "stock": 20,
            },
        )

        assert response.status_code == 400

    def test_delete_non_existent_product(self, authenticated_user):
        non_existent_product_id = (
            193019230  # Assuming this ID does not exist in the database
        )
        response = authenticated_user.delete(
            f"/api/products/{non_existent_product_id}/"
        )

        # Check that the response status code is 404 (Not Found)
        assert response.status_code == 404
        print(response.data)
        # Check response "detail" key with the specific message
        assert "detail" in response.data
        assert (
            str(response.data["detail"]) == "Not found."
        )  # Replace with your specific message

    def test_delete_invalid_product(self, authenticated_user):
        bad_product_data = baker.make("Product", price=-10.00)
        response = authenticated_user.delete(
            f"/api/products/{bad_product_data.product_id}/"
        )

        assert response.status_code == 204
        assert not response.data


# Tests for edge cases
@pytest.mark.django_db
class TestProductEdgeCases:

    endpoint = "/api/products/"

    def test_create_empty_product(self, authenticated_user):
        product = {}
        response = authenticated_user.post("/api/products/", product)

        assert response.status_code == 400

    def test_update_empty_product(self, authenticated_user):
        product = baker.make("Product")
        response = authenticated_user.patch(
            f"/api/products/{product.product_id}/",
            {},
        )

        assert response.status_code == 400
