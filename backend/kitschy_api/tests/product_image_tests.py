import pytest
from model_bakery import baker

"""
Tests:
1. TestProductImageAPI - CRUD operations
2. Edge Cases - Empty data
"""


@pytest.mark.django_db
class TestProductImageAPI:
    endpoint = "/api/products-image/"

    def test_post_product_image(self, authenticated_user):
        product = baker.make("Product")
        product_image_data = {
            "product": product.product_id,
            "img_url": "http://image.com",
            "alt_desc": "An image of the product",
        }
        response = authenticated_user.post(self.endpoint, product_image_data)

        assert response.status_code == 201
        assert response.data["product"] == product.product_id

    def test_update_product_image(self, authenticated_user):
        product_image = baker.make("ProductImage")
        response = authenticated_user.put(
            f"{self.endpoint}{product_image.product_image_id}/",
            {
                "product": product_image.product.product_id,
                "img_url": "http://updated_image.com",
                "alt_desc": product_image.alt_desc,
            },
        )

        assert response.status_code == 200

    def test_delete_product_image(self, authenticated_user):
        product_image = baker.make("ProductImage")
        response = authenticated_user.delete(
            f"{self.endpoint}{product_image.product_image_id}/"
        )

        assert response.status_code == 204
        assert not response.data


@pytest.mark.django_db
class TestProductImagesEdgeCases:
    endpoint = "/api/products-image/"

    def test_empty_data(self, authenticated_user):
        response = authenticated_user.post(self.endpoint, {})

        assert response.status_code == 400
        assert response.data["product"] == [
            "This field is required."
        ]  # Changed from product_image_id
        assert response.data["img_url"] == ["This field is required."]
        assert response.data["alt_desc"] == [
            "This field is required."
        ]  # Add this since it's required
