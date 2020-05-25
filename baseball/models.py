from django.db import models


class Sport(models.Model):
    mlb_api_sports_id = models.IntegerField()
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=100)
    sort_order = models.IntegerField()
    active = models.BooleanField()

    def __str__(self):
        return self.name


class League(models.Model):
    # http://statsapi.mlb.com/api/v1/league
    mlb_api_league_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=45, null=True, blank=True)
    abbreviation = models.CharField(max_length=5, null=True, blank=True, default='None')
    name_short = models.CharField(max_length=45, null=True, blank=True)
    sport_id = models.ForeignKey('Sport', on_delete=models.CASCADE, null=True, blank=True)
    sort_order = models.IntegerField(null=True, blank=True)
    number_of_teams = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.name


class Conferences(models.Model):
    # http://statsapi.mlb.com/api/v1/conferences
    mlb_api_conference_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=22, null=True, blank=True)
    abbreviation = models.CharField(max_length=4, null=True, blank=True)
    name_short = models.CharField(max_length=11, null=True, blank=True)
    sport_id = models.ForeignKey('Sport', on_delete=models.CASCADE, null=True, blank=True)
    league_id = models.ForeignKey('League', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Division(models.Model):
    # http://statsapi.mlb.com/api/v1/divisions
    mlb_api_division_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=15, null=True, blank=True)
    abbreviation = models.CharField(max_length=6, null=True, blank=True)
    name_short = models.CharField(max_length=15, null=True, blank=True)
    sport_id = models.ForeignKey('Sport', on_delete=models.CASCADE, null=True, blank=True)
    league_id =  models.ForeignKey('League', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    # http://statsapi.mlb.com/api/v1/teams
    mlb_api_team_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=15, null=True, blank=True)
    venue_id = models.ForeignKey('Venue', on_delete=models.CASCADE, null=True, blank=True)
    team_code = models.CharField(max_length=3, null=True, blank=True)
    file_code = models.CharField(max_length=3, null=True, blank=True)
    abbreviation = models.CharField(max_length=3, null=True, blank=True)
    team_name = models.CharField(max_length=14, null=True, blank=True)
    location_name = models.CharField(max_length=7, null=True, blank=True)
    short_name = models.CharField(max_length=5, null=True, blank=True)
    parent_organization_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    first_year_of_play = models.IntegerField(null=True, blank=True)
    sport_id = models.ForeignKey('Sport', on_delete=models.CASCADE, null=True, blank=True)
    league_id =  models.ForeignKey('League', on_delete=models.CASCADE, null=True, blank=True)
    division_id =  models.ForeignKey('Division', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class TeamHistory(models.Model):
    # http://statsapi.mlb.com/api/v1/teams/history?teamIds=119
    pass


class Venue(models.Model):
    # http://statsapi.mlb.com/api/v1/venues
    mlb_api_venue_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=23, null=True, blank=True)

    def __str__(self):
        return self.name

