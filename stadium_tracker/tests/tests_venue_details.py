# TODO: add tests for get_venue_total
from django.test import TestCase
from stadium_tracker.venue_details import get_venue_details


class TestVenueDetails(TestCase):
    def test_get_venue_details(self):
        x = get_venue_details(22)
        self.assertEqual(x, "Dodger Stadium")


