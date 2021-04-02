from django.test import Client
from django.test import TestCase
from model_bakery import baker
from api.models import UniqueidTable

class TestEndpointCreate(TestCase):
    def test_status_code(self):
        c = Client()
        response = c.get("webhook-testing/v1/endpoints/create/")
        self.assertEqual(response.status_code, 201)
