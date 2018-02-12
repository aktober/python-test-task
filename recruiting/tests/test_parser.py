from django.core.management import call_command
from django.test import TestCase

from recruiting.models import Vacancy


class TestParser(TestCase):

    def test_parse(self):
        self.assertEqual(Vacancy.objects.all().count(), 0)
        call_command('parse_trainee')
        self.assertEqual(Vacancy.objects.all().count(), 20)
