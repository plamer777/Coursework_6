"""This file contains TestComment class providing methods to test base CRUD
functionality for Comment models"""
import pytest
# -------------------------------------------------------------------------


@pytest.mark.django_db
class TestComment:
    """The TestComment class with necessary methods for testing"""
    def test_comment_list(
            self, client, comment_list_expected, token_and_user) -> None:
        """This method tests a 'list' action of the ViewSet for Comment entities
        :param client: a test client to send requests and receive responses
        :param comment_list_expected: a fixture with the expected results
        """
        results = comment_list_expected.get('results')
        token = token_and_user[0]
        ad_id = results[0]['ad_id']

        response = client.get(f'/api/ads/{ad_id}/comments/',
                              HTTP_AUTHORIZATION=f'Bearer {token}',
                              content_type='application/json')

        response.data['results'][0]['created_at'] = results[0]['created_at']
        self._check_response(response, 200, comment_list_expected)

    def test_comment_retrieve_unauthorized(self, client, comment) -> None:
        """This method tests a 'retrieve' action of the ViewSet for Comment
        entities when a user is not authorized
        :param client: a test client to send requests and receive responses
        :param comment: the factory created Comment instances
        """
        response = client.get(f'/api/ads/{comment.ad.pk}/comments'
                              f'/{comment.pk}/')

        assert response.status_code == 401

    def test_comment_retrieve_authorized(self, client,
                                         comment_retrieve_expected,
                                         token_and_user) -> None:
        """This method tests a 'retrieve' action of the ViewSet for Comment
        entities when a user is authorized
        :param client: a test client to send requests and receive responses
        :param comment_retrieve_expected: expected result to compare with
        :param token_and_user: a fixture returning a token and user instance
        """
        ad_pk = comment_retrieve_expected.get('ad_id')
        comment_pk = comment_retrieve_expected.get('pk')
        token = token_and_user[0]
        response = client.get(f'/api/ads/{ad_pk}/comments/{comment_pk}/',
                              HTTP_AUTHORIZATION=f'Bearer {token}')
        response.data['created_at'] = comment_retrieve_expected['created_at']

        self._check_response(response, 200, comment_retrieve_expected)

    def test_comment_create(self, client, token_and_user,
                            ad, comment_create_expected,
                            new_comment) -> None:
        """This method tests a 'create' action of the ViewSet for Comment
        entities
        :param client: a test client to send requests and receive responses
        :param new_comment: a fixture providing a new comment to test 'create'
        action of the ViewSet
        :param token_and_user: a fixture returning a token and user instance
        """
        token = token_and_user[0]
        response = client.post(f'/api/ads/{ad.pk}/comments/',
                               data=new_comment,
                               HTTP_AUTHORIZATION=f'Bearer {token}')
        expected = comment_create_expected
        expected['ad_id'] = ad.pk
        response.data['created_at'] = None
        expected['pk'] = response.data.get('pk')

        self._check_response(response, 201, expected)

    def test_comment_update(
            self, client, token_and_user, updated_comment) -> None:
        """This method tests an 'update' action of the ViewSet for Comment
        entities
        :param client: a test client to send requests and receive responses
        :param updated_comment: a fixture providing a data for Comment model to
        update
        :param token_and_user: a fixture returning a token and user instance
        """
        token = token_and_user[0]
        user = token_and_user[1]
        expected = updated_comment[0].copy()
        comment_id = updated_comment[1]
        ad_id = expected.get('ad_id')

        expected.update({
            'author_image': None,
            'pk': comment_id,
            "author_id": user.pk,
            "author_first_name": user.first_name,
            "author_last_name": user.last_name,
        })

        response = client.put(f'/api/ads/{ad_id}/comments/{comment_id}/',
                              data=updated_comment[0],
                              HTTP_AUTHORIZATION=f'Bearer {token}',
                              content_type='application/json')

        self._check_response(response, 200, expected)

    def test_comment_delete(self, client, token_and_user, add_comment):
        """This method tests an 'destroy' action of the ViewSet for Comment
        entities
        :param client: a test client to send requests and receive responses
        :param add_comment: a fixture providing a data for Comment model to
        delete
        :param token_and_user: a fixture returning a token and user instance
        """
        token = token_and_user[0]
        ad_id = add_comment.get('ad_id')
        comment_id = add_comment.get('pk')

        response = client.delete(f'/api/ads/{ad_id}/comments/{comment_id}/',
                                 HTTP_AUTHORIZATION=f'Bearer {token}')

        assert response.status_code == 204
        assert response.data is None

    @staticmethod
    def _check_response(response, status_code, expected):
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
