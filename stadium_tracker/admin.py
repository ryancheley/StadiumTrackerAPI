from django.contrib import admin
from .models import GameDetails, League, Division, Venue, Team

admin.site.register(GameDetails)
admin.site.register(League)
admin.site.register(Division)
admin.site.register(Venue)
admin.site.register(Team)
