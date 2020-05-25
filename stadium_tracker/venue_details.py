import requests
from django.db.models import Count
from stadium_tracker.models import GameDetails


def get_venue_details(venue_id):
    url = f"http://statsapi.mlb.com/api/v1/venues/{venue_id}"
    response = requests.get(url)
    venue_name = None
    if response.status_code == 200:
        venue_name = response.json().get("venues")[0].get("name")
    return venue_name


def get_venue_total(venue_id):
    venue_total = list(
        GameDetails.objects.all()
        .values("venue_id")
        .annotate(total=Count("venue_id"))
        .filter(venue_id=venue_id)
        .values("total")
    )
    return venue_total

