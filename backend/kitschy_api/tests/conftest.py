import pytest
from model_bakery import baker
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    """ "Return API client for public endpoints"""
    return APIClient()


@pytest.fixture
def user():
    return baker.make("kitschy_api.User")


@pytest.fixture
def authenticated_user(api_client, user):
    """Return API client for authenticated user"""
    api_client.force_authenticate(user=user)
    return api_client


# TODO: Admin user fixture
