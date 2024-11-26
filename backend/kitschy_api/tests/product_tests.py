import pytest
from model_bakery import baker


# NOTE: Negative values in stock represent pre-orders



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

    def test_delete_invalid_product(self, authenticated_user):
        invalid_product = baker.make("Product", price=-10)
        response = authenticated_user.delete(
            f"/api/products/{invalid_product.product_id}/"
        )

        assert response.status_code == 204
        assert not response.data
