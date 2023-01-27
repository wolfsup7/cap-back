from django.test import TestCase
from clients_api.models import Client

class TestModel(TestCase):
    def test_should_create_client(self):
        client=Client.objects.create(name="Quinn", breed="chi", age=1, picture="https://www.akc.org/wp-content/uploads/2017/11/Chihuahua-standing-in-three-quarter-view.jpg", address="1010 safe way", phone="222-333-4444", appointment="every day")
        client.save()

        self.assertEqual(client.name, "Quinn")
        self.assertEqual(client.breed, "chi")
        self.assertEqual(client.age, 1)
        self.assertEqual(client.picture, "https://www.akc.org/wp-content/uploads/2017/11/Chihuahua-standing-in-three-quarter-view.jpg")
        self.assertEqual(client.address, "1010 safe way")
        self.assertEqual(client.phone, "222-333-4444")
        self.assertEqual(client.appointment, "every day")


if __name__ == '__main__':
    TestCase.main()

