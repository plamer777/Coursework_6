"""This file contains fixtures to test CRUD for Comment entities"""
from typing import Any, OrderedDict
import pytest
# --------------------------------------------------------------------------


@pytest.fixture
def comment_list_expected(comment) -> dict[str, Any]:
    """This fixture returns an expected data to test a 'list' action"""
    expected = {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [
            {
                "pk": comment.pk,
                "ad_id": comment.ad.pk,
                "author_id": comment.author.pk,
                "author_first_name": comment.author.first_name,
                "author_last_name": comment.author.last_name,
                "author_image": None,
                "text": comment.text,
                "created_at": str(comment.created_at)
            }
        ]
    }

    return expected


@pytest.fixture
def comment_retrieve_expected(comment) -> dict[str, Any]:
    """This fixture returns an expected data to test a 'retrieve' action"""
    expected = {
        "pk": comment.pk,
        "ad_id": comment.ad.pk,
        "author_id": comment.author.pk,
        "author_first_name": comment.author.first_name,
        "author_last_name": comment.author.last_name,
        "author_image": None,
        "text": comment.text,
        "created_at": str(comment.created_at)

    }
    return expected


@pytest.fixture
def new_comment() -> dict[str, str]:
    """This fixture returns data to create a new comment"""
    comment_data = {
        "text": "Great thing"
    }

    return comment_data


@pytest.fixture
def comment_create_expected(token_and_user, new_comment) -> dict[str, Any]:
    """This fixture provides an expected data to test a 'create' action of the
    ViewSet"""
    user = token_and_user[1]
    expected = {
        "author_id": user.pk,
        "author_first_name": user.first_name,
        "author_last_name": user.last_name,
        "author_image": None,
        "text": new_comment.get('text'),
        "created_at": None
    }

    return expected


@pytest.fixture
def add_comment(
        new_comment, token_and_user, client, ad) -> OrderedDict[str, Any]:
    """This fixture creates a new comment and returns expected data"""
    token = token_and_user[0]
    response = client.post(f'/api/ads/{ad.pk}/comments/',
                           data=new_comment,
                           HTTP_AUTHORIZATION=f'Bearer {token}')

    return response.data


@pytest.fixture
def updated_comment(add_comment) -> tuple[dict, int]:
    """This fixture provides an expected data to test an 'update' action"""
    comment_pk = add_comment.get('pk')
    updated = {
        "text": "I've changed my opinion",
        "created_at": add_comment.get('created_at'),
        "ad_id": add_comment.get('ad_id'),
    }

    return updated, comment_pk
