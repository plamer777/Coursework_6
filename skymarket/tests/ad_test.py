"""This file contains TestAd class providing methods to test base CRUD
functionality for Ad models"""
import pytest
# -------------------------------------------------------------------------


@pytest.mark.django_db
class TestAd:
    """The TestAd class with necessary methods for testing"""
    def test_ad_list(self, client, ad_list_expected) -> None:
        """This method tests a 'list' action of the ViewSet for Ad entities
        :param client: a test client to send requests and receive responses
        :param ad_list_expected: a fixture with the expected results
        """
        response = client.get('/api/ads/')
        self._check_response(response, 200, ad_list_expected)

    def test_ad_retrieve_unauthorized(self, client, ad) -> None:
        """This method tests a 'retrieve' action of the ViewSet for Ad entities
        when a user is not authorized
        :param client: a test client to send requests and receive responses
        :param ad: the factory created Ad instances
        """
        response = client.get('/api/ads/1/')

        assert response.status_code == 401

    def test_ad_retrieve_authorized(self, client, ad_retrieve_expected,
                                    token_and_user) -> None:
        """This method tests a 'retrieve' action of the ViewSet for Ad entities
        when a user is authorized
        :param client: a test client to send requests and receive responses
        :param ad_retrieve_expected: expected result to compare with
        :param token_and_user: a fixture returning a token and user instance
        """
        ad_pk = ad_retrieve_expected.get('pk')
        token = token_and_user[0]
        response = client.get(f'/api/ads/{ad_pk}/',
                              HTTP_AUTHORIZATION=f'Bearer {token}')

        self._check_response(response, 200, ad_retrieve_expected)

    def test_ad_create(self, client, token_and_user, new_ad) -> None:
        """This method tests a 'create' action of the ViewSet for Ad entities
        :param client: a test client to send requests and receive responses
        :param new_ad: a fixture providing a new ad to test 'create' action
        of the ViewSet
        :param token_and_user: a fixture returning a token and user instance
        """
        token = token_and_user[0]
        response = client.post('/api/ads/',
                               data=new_ad,
                               HTTP_AUTHORIZATION=f'Bearer {token}')
        expected = new_ad
        expected['image'] = None
        expected['pk'] = response.data.get('pk')

        self._check_response(response, 201, expected)

    def test_ad_update(self, client, token_and_user, updated_ad) -> None:
        """This method tests an 'update' action of the ViewSet for Ad
        entities
        :param client: a test client to send requests and receive responses
        :param updated_ad: a fixture providing a data for Ad model to update
        :param token_and_user: a fixture returning a token and user instance
        """
        token = token_and_user[0]
        user = token_and_user[1]
        expected = updated_ad[0].copy()
        ad_id = updated_ad[1]
        expected.update({
            'image': None,
            'pk': ad_id,
            "phone": user.phone,
            "author_id": user.pk,
            "author_first_name": user.first_name,
            "author_last_name": user.last_name,
        })

        response = client.put(f'/api/ads/{ad_id}/',
                              data=updated_ad[0],
                              HTTP_AUTHORIZATION=f'Bearer {token}',
                              content_type='application/json')

        self._check_response(response, 200, expected)

    def test_ad_delete(self, client, token_and_user, create_ad) -> None:
        """This method tests an 'destroy' action of the ViewSet for Ad
        entities
        :param client: a test client to send requests and receive responses
        :param create_ad: a fixture providing a data for Ad model to delete
        :param token_and_user: a fixture returning a token and user instance
        """
        token = token_and_user[0]
        ad_id = create_ad.get('pk')

        response = client.delete(f'/api/ads/{ad_id}/',
                                 HTTP_AUTHORIZATION=f'Bearer {token}')

        assert response.status_code == 204
        assert response.data is None

    @staticmethod
    def _check_response(response, status_code, expected) -> None:
        """This method serves to test the response from the API and extracted
        data
        :param response: an instance of WSGIRequest
        :param status_code: an integer indicating the status code to check
        :param expected: a json-like object containing the expected data to
        compare with
        """
        assert response.status_code == status_code
        assert response.data is not None
        assert response.data == expected
