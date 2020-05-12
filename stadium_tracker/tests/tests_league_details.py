from django.test import TestCase
from users.models import CustomUser
from stadium_tracker.league_details import (
    get_team_division,
    get_division_details,
    get_leagues,
)


class LeagueDetailsTest(TestCase):
    def test_get_team_division(self):
        x = get_team_division(1, 119)
        self.assertEqual(x, 203)

    def test_get_team_division_no_team(self):
        x = get_team_division(1, None)
        self.assertEqual(x, 200)

    def test_get_division_details(self):
        user = CustomUser.objects.create_user(username="ryan", favorite_team=108)
        x = get_division_details(1, user)
        self.assertEqual(x[5]["default_division"], True)

    def test_get_division_details_none_user(self):
        x = get_division_details(1, None)
        self.assertEqual(x[0].get("division_id"), 202)

    def test_get_leagues_mlb_is_first(self):
        x = get_leagues()
        self.assertEqual(x[0]["name"], "Major League Baseball")

    def test_get_leagues_len(self):
        x = get_leagues()
        self.assertEqual(len(x), 21)
