from django.test import TestCase

from recruiting.models import City, Company


class TestModels(TestCase):

    def test_city_creation(self):
        city = City.objects.create(name='Kiev')
        self.assertEqual(City.objects.all().count(), 1)
        self.assertEqual(city.name, 'Kiev')

    def test_company_creation(self):
        company = Company.objects.create(
            name="test name",
            location="test location"
        )
        self.assertEqual(Company.objects.all().count(), 1)
        self.assertEqual(company.name, 'test name')
        self.assertEqual(company.location, 'test location')

    def test_vacancy_creation(self):
        #todo
        pass