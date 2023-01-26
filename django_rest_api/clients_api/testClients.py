from django.test import TestCase
from clients_api.models import Client


class ClientTestCase(TestCase):
    def testClient(self):
        client = Client(name="Name", breed="Breed", age=1, picture="URL", address="Add", phone="Phone", appointment="Schedule")
        self.assertEqual(client.name, "Name")
        self.assertEqual(client.breed, "Breed")
        self.assertEqual(client.age, 1)
        self.assertEqual(client.picture, "URL")
        self.assertEqual(client.address, "Add")
        self.assertEqual(client.phone, "Phone")
        self.assertEqual(client.appointment, "Schedule")
