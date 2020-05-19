from django.db import migrations
from stadium_tracker.league_details import get_leagues
from stadium_tracker.models import Leagues


def load_leagues(apps, schema_editor):
    for league in get_leagues():
        Leagues(mlb_api_league_id=league['id'],
                league_name=league['name'],
                ).save()


class Migration(migrations.Migration):

    dependencies = [
        ('stadium_tracker', '0013_leagues_mlb_api_league_id'),
    ]

    operations = [
        migrations.RunPython(load_leagues),
    ]
