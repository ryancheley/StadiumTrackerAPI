import requests


def get_venues():
    url = 'http://statsapi.mlb.com/api/v1/venues'
    response = requests.get(url)
    venues = response.json().get('venues')
    venues = [d for d in venues if d['id'] in range(0,33)]
    venues = sorted(venues, key = lambda venue: (venue['name']))
    venue_display = []
    for i in range(len(venues)):
        venue_display.append({'id': venues[i].get('id'), 'name': venues[i].get('name')})
    return venue_display


def get_venue_details(venue_id):
    url = f'http://statsapi.mlb.com/api/v1/venues/{venue_id}'
    response = requests.get(url)
    venue_name = response.json().get('venues')[0].get('name')
    return venue_name
