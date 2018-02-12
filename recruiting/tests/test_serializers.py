from django.test import TestCase

from recruiting.api.serializers import CitySerializer, CompanySerializer, VacancySerializer
from recruiting.models import City, Company, Vacancy


class TestCitySerializer(TestCase):

    def setUp(self):
        self.city_attributes = {'name': 'London'}
        self.serializer_data = {'name': 'Berlin'}
        self.city = City.objects.create(**self.city_attributes)
        self.serializer = CitySerializer(instance=self.city)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['name']))

    def test_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['name'], self.city_attributes['name'])

    def test_name_data_correctly_saves(self):
        self.serializer_data['name'] = 'Kiev'
        serializer = CitySerializer(data=self.serializer_data)
        serializer.is_valid()
        new_city = serializer.save()
        new_city.refresh_from_db()
        self.assertEqual(new_city.name, 'Kiev')


class TestCompanySerializer(TestCase):

    def setUp(self):
        self.company_attributes = {'name': 'ALDI', 'location': 'Berlin'}
        self.serializer_data = {'name': 'SomeName', 'location': 'NY'}
        self.company = Company.objects.create(**self.company_attributes)
        self.serializer = CompanySerializer(instance=self.company)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['name', 'location']))

    def test_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['name'], self.company_attributes['name'])

    def test_location_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['location'], self.company_attributes['location'])

    def test_name_data_correctly_saves(self):
        self.serializer_data['name'] = 'SomeName'
        serializer = CompanySerializer(data=self.serializer_data)
        serializer.is_valid()
        new_company = serializer.save()
        new_company.refresh_from_db()
        self.assertEqual(new_company.name, 'SomeName')

    def test_location_data_correctly_saves(self):
        self.serializer_data['location'] = 'SomeCity'
        serializer = CompanySerializer(data=self.serializer_data)
        serializer.is_valid()
        new_company = serializer.save()
        new_company.refresh_from_db()
        self.assertEqual(new_company.location, 'SomeCity')


class TestVacancySerializer(TestCase):

    def setUp(self):
        company1 = Company.objects.create(name='Company1', location='location1')
        company2 = Company.objects.create(name='Company2', location='location2')
        self.vacancy_attributes = {
            'is_active': True,
            'title': 'Some title',
            'starts_at': '01.04.2018',
            'ends_at': '15 Monate',
            'description': 'Some description',
            'company': company1
        }
        self.serializer_data = {
            'is_active': True,
            'title': 'Some another title',
            'starts_at': '01.06.2018',
            'ends_at': '5 Monate',
            'description': 'Some other description',
            'company': company2
        }
        self.vacancy = Vacancy.objects.create(**self.vacancy_attributes)
        self.serializer = VacancySerializer(instance=self.vacancy)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['is_active', 'title', 'location',
                                                'starts_at', 'ends_at', 'description',
                                                'image_list', 'company']))

    def test_title_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['title'], self.vacancy_attributes['title'])

    def test_company_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['company'].get('name'), self.vacancy_attributes['company'].name)
        self.assertEqual(data['company'].get('location'), self.vacancy_attributes['company'].location)
