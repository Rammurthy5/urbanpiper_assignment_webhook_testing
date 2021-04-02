from django.test import Client
from django.test import TestCase
from model_bakery import baker
from api.models import UniqueidTable


class TestPostEndpoint(TestCase):
    def test_data_push(self):
        c = Client()
        u = UniqueidTable.objects.create()
        u.save()
        response = c.post("webhook-testing/v1/endpoints/{}/post".format(u.uniqueid), data={"data": "hello hello"})
        UniqueidTable.objects.filter(uniqueid=u.uniqueid).delete()
        self.assertEqual(response.status_code, 201)
    