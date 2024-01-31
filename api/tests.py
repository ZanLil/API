from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import PerevalAdded


class SubmitDataTests(APITestCase):
    """Класс для тестирования API."""

    def setUp(self):
        """Начальная конфигурация"""
        self.user = User.objects.create_user(username='testuser', password='testpassword', email='user@mail.ru')
        self.url_submit_data = '/api/v1/submit-data/'
        self.url_submit_data_detail = '/api/v1/submit-data/{}/'.format(1)

    def test_submit_data_create(self):
        data = {
            "raw_data": {
                "user": {
                    "fam": "fam",
                    "otc": "otc",
                    "name": "name",
                    "email": "email",
                    "phone": "number"
                },
                "level": {
                    "autumn": "1A",
                    "spring": "",
                    "summer": "1A",
                    "winter": ""
                },
                "title": "Кавказские горы",
                "coords": {
                    "height": "1200",
                    "latitude": "127.00",
                    "longitude": "68.22"
                },
                "connect": "",
                "add_time": "2024.01.31 12:09:00",
                "beautyTitle": "Кавка",
                "other_titles": ""
            },
            "images": [
                {
                    "id": 1,
                    "title": ""
                }
            ]
        }
        response = self.client.post(self.url_submit_data, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(PerevalAdded.objects.count(), 1)

    def test_submit_data_create_invalid_data(self):
        data = {}
        response = self.client.post(self.url_submit_data, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_data_by_user_email_authenticated_user(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url_submit_data, {'user__email': self.user.email})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], status.HTTP_200_OK)
        self.assertIsNotNone(response.data['data'])

    def test_get_data_by_user_email_anonymous_user(self):
        response = self.client.get(self.url_submit_data, {'user__email': 'some@example.com'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_data_by_user_email_no_email_provided(self):
        response = self.client.get(self.url_submit_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_data_detail_valid_id(self):
        data = {
            "raw_data": {
                "user": {
                    "fam": "fam",
                    "otc": "otc",
                    "name": "name",
                    "email": "email",
                    "phone": "number"
                },
                "level": {
                    "autumn": "1A",
                    "spring": "",
                    "summer": "1A",
                    "winter": ""
                },
                "title": "Кавказские горы",
                "coords": {
                    "height": "1200",
                    "latitude": "127.00",
                    "longitude": "68.22"
                },
                "connect": "",
                "add_time": "2024.01.31 12:09:00",
                "beautyTitle": "Кавка",
                "other_titles": ""
            },
            "images": [
                {
                    "id": 1,
                    "title": ""
                }
            ]
        }
        resp = self.client.post(self.url_submit_data, data, format='json')
        response = self.client.get(self.url_submit_data_detail)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data)

    def test_get_data_detail_invalid_id(self):
        invalid_url = '/v1/submit-data/{}/'.format(999)
        response = self.client.get(invalid_url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_data_invalid_id(self):
        invalid_url = '/v1/submit-data/{}/'.format(999)
        response = self.client.patch(invalid_url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
