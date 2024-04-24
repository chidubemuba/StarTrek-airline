from django.test import TestCase
from flights.models import Flight

# Create your tests here.
class FlightModelTestCase(TestCase):
    def test_str_representation(self):
        flight = Flight(id=1, origin="New York", destination="Los Angeles")
        expected_str = "1: New York to Los Angeles"
        self.assertEqual(str(flight), expected_str)