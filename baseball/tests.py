from django.test import TestCase
from baseball.models import Sport, League, Conferences, Division, Team, Venue


class SportTest(TestCase):

    def test_string_representation(self):
        sport = Sport.objects.filter(mlb_api_sports_id=1).first()
        self.assertEqual(str(sport), "Major League Baseball")


class LeagueTest(TestCase):

    def test_string_representation(self):
        league = League.objects.filter(mlb_api_league_id=103).first()
        self.assertEqual(str(league), "American League")


class ConferencesTest(TestCase):

    def test_string_representation(self):
        conference = Conferences.objects.filter(mlb_api_conference_id=301).first()
        self.assertEqual(str(conference), 'PCL American Conference')


class DivisionTest(TestCase):

    def test_string_representation(self):
        division_name = Division.objects.filter(mlb_api_division_id=201).first()
        self.assertEqual(str(division_name), 'American League East')


class TeamTest(TestCase):

    def test_string_representation(self):
        team = Team.objects.filter(mlb_api_team_id=119).first()
        self.assertEqual(str(team), 'Los Angeles Dodgers')


class VenueTest(TestCase):

    def test_string_representation(self):
        venue = Venue.objects.filter(mlb_api_venue_id=22).first()
        self.assertEqual(str(venue), 'Dodger Stadium')
