from django.contrib.auth.models import AbstractUser
from django.db import models
import statsapi


class CustomUser(AbstractUser):
    team_choices = []
    teams = statsapi.lookup_team('', sportIds=1)
    for t in teams:
        team_choices.append((t.get("id"), t.get("name")))
    favorite_team = models.IntegerField(choices=team_choices, blank=True, null=True,)
