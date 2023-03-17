"""This file contains fixtures to test CRUD for Ad entities"""
from typing import Any, OrderedDict
import pytest
# --------------------------------------------------------------------------


@pytest.fixture()
def new_ad(token_and_user) -> dict[str, Any]:
    user = token_and_user[1]
    """This fixture provides a data to test a 'create' action of the ViewSet"""
    ad_data = {
        "title": 'My new advertisement',
        "description": 'It costs to buy',
        "price": 1000,
        "phone": user.phone,
        "author_id": user.pk,
        "author_first_name": user.first_name,
        "author_last_name": user.last_name,
    }

    return ad_data


@pytest.fixture
def create_ad(client, token_and_user, new_ad) -> OrderedDict[str, Any]:
    """This fixture provides a data to test an 'delete' action of
    the ViewSet"""
    token = token_and_user[0]
    response = client.post('/api/ads/',
                           data=new_ad,
                           HTTP_AUTHORIZATION=f'Bearer {token}')

    return response.data


@pytest.fixture
def updated_ad(create_ad) -> tuple[dict, int]:
    """This fixture provides a data to test an 'update' action of
    the ViewSet"""
    ad_pk = create_ad.get('pk')
    updated = {
        "title": "New_title",
        "description": "New_description",
        "price": create_ad.get('price')
    }

    return updated, ad_pk


@pytest.fixture
def ad_list_expected(ad) -> dict[str, Any]:
    """This fixture returns an expected data to test a 'list' action"""
    expected = {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [
            {
                "image": None,
                "title": ad.title,
                "description": ad.description,
                "price": ad.price,
                "pk": ad.pk,
            }
        ]
    }

    return expected


@pytest.fixture
def ad_retrieve_expected(ad) -> dict[str, Any]:
    """This fixture returns an expected data to test a 'retrieve' action"""
    expected = {
        "pk": ad.pk,
        "title": ad.title,
        "description": ad.description,
        "price": ad.price,
        "image": None,
        "phone": ad.author.phone,
        "author_id": ad.author.pk,
        "author_first_name": ad.author.first_name,
        "author_last_name": ad.author.last_name,
    }

    return expected
