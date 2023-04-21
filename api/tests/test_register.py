from rest_framework.test import APITestCase
from rest_framework import status


class RegisterViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_register_user_with_data(self):
        url = '/api/register/'

        data = {
            'email': 'test@example.com',
            'username': 'testuser',
            'password': 'AbcDeFc123!',
        }
        response = self.client.post(url, data=data)

        assert response.status_code == status.HTTP_200_OK

    def test_register_user_without_data(self):
        url = '/api/register/'

        data = {}
        response = self.client.post(url, data=data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_register_user_with_existing_email(self):
        url = '/api/register/'
        data = {
            'email': 'test@example.com',
            'username': 'testuser',
            'password': 'Test123!',
        }
        self.client.post(url, data=data)

        data = {
            'email': 'test@example.com',
            'username': 'testuser2',
            'password': 'Test123!',
        }
        response = self.client.post(url, data=data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_register_user_with_weak_password(self):
        url = '/api/register/'
        data = {
            'email': 'test2@example.com',
            'username': 'testuser2',
            'password': 'password',
        }
        response = self.client.post(url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
