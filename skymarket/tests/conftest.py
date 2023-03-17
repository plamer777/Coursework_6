"""This file contains fixtures and register factories for testing purposes"""
import pytest
from pytest_factoryboy import register
from tests.factories import AdFactory, CommentFactory, UserFactory
# ------------------------------------------------------------------------

register(UserFactory)
register(AdFactory)
register(CommentFactory)

pytest_plugins = ['tests.fixtures.ad_fixtures',
                  'tests.fixtures.comment_fixtures']


@pytest.fixture
@pytest.mark.django_db
def token_and_user(client, django_user_model) -> tuple:
    """A fixture returning token and user instance"""
    new_user = {
        'email': 'legat777@mail.ru',
        'password': 'qwerty12345',
        'role': 'user',
        'first_name': 'name',
        'last_name': 'surname',
        'phone': '+79052039898'
    }
    user = django_user_model.objects.create_user(**new_user)

    response = client.post('/api/token/', data=new_user, format='json')
    user_token = response.data.get('access')

    return user_token, user
