from django.test import Client
from django.test import TestCase
from model_bakery import baker
from api.models import UniqueidTable


class TestListEndpoint(TestCase):
        
    def test_list_of_endpoints(self):
        c = Client()
        response = c.get("webhook-testing/v1/endpoints/")
        self.assertTrue(response.json()>=1)
