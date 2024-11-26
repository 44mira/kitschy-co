import pytest
from model_bakery import baker

""" Sample tests:
  2. GET api/products/{product_id} - get a single product
  3. POST api/products/ - create a new product
  4. PUT api/products/{product_id} - update a product
  5. DELETE api/products/{product_id} - delete a product
"""


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
            "quantity": 10,
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
                "quantity": 20,
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
