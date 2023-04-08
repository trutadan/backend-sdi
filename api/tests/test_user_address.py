from django.test import TestCase

from api.models import UserAddress


class UserAddressModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        UserAddress.objects.create(street="Strada General Vasile Milea", city="Bucharest", state="Bucharest", country="Romania", zip_code="061344")

    def test_string_method(self):
        address = UserAddress.objects.get(city="Bucharest", zip_code="061344")
        expected_address_string = "061344, Strada General Vasile Milea, Bucharest, Romania"
        self.assertEqual(str(address), expected_address_string)
