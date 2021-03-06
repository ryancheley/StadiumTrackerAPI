# Generated by Django 3.0.6 on 2020-05-20 02:22

from django.db import migrations
import requests
from stadium_tracker.models import Division, League


def load_divisions(apps, schema_editor):
    url = 'http://statsapi.mlb.com/api/v1/divisions'
    r = requests.get(url)
    divisions = r.json()['divisions']
    for division in divisions:
        Division(
            mlb_api_division_id=division['id'],
            division_name=division['name'],
            mlb_api_league_id=division['sport']['id'],
            mlb_api_sport_id=League.objects.filter(mlb_api_league_id=division['sport']['id'])[0],
            has_wildcard=division['hasWildcard'],
        ).save()


class Migration(migrations.Migration):

    dependencies = [
        ('stadium_tracker', '0019_auto_20200520_0228'),
    ]

    operations = [
        migrations.RunPython(load_divisions),
    ]
