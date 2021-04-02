import uuid
from django.test import TestCase
from model_bakery import baker
from django.db.utils import IntegrityError
from django.db.transaction import TransactionManagementError
from api.models import UniqueidTable, DataTable


class TestModels(TestCase):
    
    def cleanup(self, *args):
        for i in args:
            UniqueidTable.objects.filter(uniqueid=i.uniqueid).delete()

    def test_uuid_duplicates(self):
        input_1 = UniqueidTable(uniqueid=str(uuid.uuid4()))
        input_2 = UniqueidTable(uniqueid=str(uuid.uuid4()))
        self.assertNotEqual(input_1.uniqueid, input_2.uniqueid, "UUID unique creation failed")
        self.cleanup(input_1, input_2)
    
    def test_model_str(self):
        input_1 = UniqueidTable()
        input_2 = DataTable(uniqueid=input_1, data="hello there!")
        self.assertNotEqual(str(input_1), None)
        self.assertEqual(str(input_2), "hello there!")
        # self.cleanup(input_1)

    def test_uniqueid_model(self):
        uniqueid_data = baker.make(UniqueidTable)
        self.assertTrue(uniqueid_data.url.endswith(".com/"))
        self.cleanup(uniqueid_data)

    def test_data_model(self):
        data_model = baker.make(DataTable)
        self.assertTrue(data_model.__str__() is not None)
        self.cleanup(data_model.uniqueid)

    def test_data_model_quantity(self):
        data_model = baker.prepare(DataTable, _quantity=3)
        self.assertEqual(len(data_model), 3)
        self.cleanup(data_model[0])