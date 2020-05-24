from django.db import models
from StadiumTrackerAPI import settings
from django.utils import timezone


class GameDetails(models.Model):
    VIEWING_OPTIONS = (
        ('T', 'Television'),
        ('P', 'In Person')
    )

    home_team = models.CharField(max_length=100)
    home_runs = models.IntegerField()
    home_hits = models.IntegerField(blank=True, null=True)
    home_errors = models.IntegerField(blank=True, null=True)
    away_team = models.CharField(max_length=100)
    away_runs = models.IntegerField()
    away_hits = models.IntegerField(blank=True, null=True)
    away_errors = models.IntegerField(blank=True, null=True)
    game_datetime = models.DateTimeField()
    game_headline = models.CharField(max_length=254, blank=True, null=True)
    game_body = models.TextField(blank=True, null=True)
    game_id = models.IntegerField()
    venue_id = models.IntegerField()
    stadium = models.ForeignKey('baseball.Venue', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now_add=True)
    view_type = models.CharField(max_length=1, choices=VIEWING_OPTIONS, default='P')

    def __str__(self):
        return f'{self.home_team} vs {self.away_team} ({self.game_datetime.strftime("%m/%d/%Y")})'

    def save(self, *args, **kwargs):
        self.modify_date = timezone.now()
        super(GameDetails, self).save(*args, **kwargs)

    class Meta:
        unique_together = ["user", "game_id"]
        ordering = ["user", "-game_datetime"]


class League(models.Model):
    mlb_api_league_id = models.IntegerField()
    league_name = models.CharField(max_length=255)

    def __str__(self):
        return self.league_name


class Division(models.Model):
    mlb_api_division_id = models.IntegerField()
    division_name = models.CharField(max_length=255)
    mlb_api_league_id = models.IntegerField()
    mlb_api_sport_id = models.ForeignKey('League', on_delete=models.CASCADE)
    has_wildcard = models.BooleanField()

    def __str__(self):
        return self.division_name


class Venue(models.Model):
    mlb_api_venue_id = models.IntegerField()
    venue_name = models.CharField(max_length=255)
    # ToDo: add address information

    def __str__(self):
        return self.venue_name


class Team(models.Model):
    mlb_api_team_id = models.IntegerField()
    name = models.CharField(max_length=255)
    venue = models.ForeignKey('Venue', on_delete=models.CASCADE)
    team_code = models.CharField(max_length=255)
    file_code = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=255)
    team_name = models.CharField(max_length=255)
    location_name = models.CharField(max_length=255)
    first_year_of_play = models.IntegerField()
    # league = ?
    division = models.ForeignKey('Division', on_delete=models.CASCADE)
    sport = models.ForeignKey('League', on_delete=models.CASCADE)
    short_name = models.CharField(max_length=255)
    parent_organization_id = models.ForeignKey('self', on_delete=models.CASCADE)
    all_star_status = models.BooleanField()
    active = models.BooleanField()
    spring_league = models.ForeignKey('League', on_delete=models.CASCADE, related_name='spring_league')
    # conference = ?
