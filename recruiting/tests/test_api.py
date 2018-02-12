from django.test import TestCase


class VacanciesApiTest(TestCase):

    def setUp(self):
        self.list_url = '/api/vacancies/'

    def test_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)