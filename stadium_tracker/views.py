from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from django.db.models import Count
from django.db import IntegrityError
from stadium_tracker.game_details import (
    get_game_date,
    get_boxscore,
    get_teams,
    get_game_recap,
    get_venue_id,
    get_form_details,
    get_default_game,
)
from stadium_tracker.venue_details import get_venue_details

from stadium_tracker.models import GameDetails
from baseball.models import League, Division, Sport, Team
from stadium_tracker.forms import GameDetailsForm

PAGINATION_DEFAULT = 5


class GamesViewList(ListView):
    model = GameDetails
    context_object_name = "game_list"
    template_name = "stadium_tracker/game_list.html"
    paginate_by = PAGINATION_DEFAULT
    queryset = GameDetails.objects.all()

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["pages"] = {"header": "List of Games"}
        return data


class MyGamesViewList(LoginRequiredMixin, GamesViewList):

    def get_queryset(self):
        user = self.request.user
        queryset = GameDetails.objects.filter(user_id=user)
        return queryset

    def get_context_data(self, **kwargs):
        user = self.request.user
        data = super().get_context_data(**kwargs)
        data["pages"] = {"header": f"List of Games for {str(user).title()}"}
        return data


class StadiumGamesViewList(GamesViewList):

    def get_queryset(self):
        queryset = GameDetails.objects.filter(
            venue_id=self.kwargs["venue_id"]
        ).order_by("-game_datetime")
        return queryset

    def get_context_data(self, **kwargs):
        venue_id = self.kwargs["venue_id"]
        venue = get_venue_details(venue_id)
        data = super().get_context_data(**kwargs)
        data["venue"] = venue
        data["pages"] = {"header": f"List of Games for {venue}"}
        return data


class GameDetailView(DetailView):
    model = GameDetails
    context_object_name = "details"
    template_name = "stadium_tracker/gamedetails_view.html"


class GameDetailCreate(LoginRequiredMixin, CreateView):
    model = GameDetails
    form_class = GameDetailsForm
    template_name = "stadium_tracker/gamedetails_create.html"
    success_url = reverse_lazy("stadium_tracker:my_game_list")

    def get(self, request, *args, **kwargs):
        form = GameDetailsForm()
        leagues = League.objects.all().order_by('mlb_api_league_id')
        teams = get_teams(1)
        display_dates = get_form_details(request)
        default_values = get_default_game(1)
        try:
            game_id = display_dates[0].get("gamePk")
            headline = get_game_recap(game_id, "headline")
            body = get_game_recap(game_id, "body")
            home_details = get_boxscore(game_id, "home")
            away_details = get_boxscore(game_id, "away")
            game_date = get_game_date(game_id, 1)

            form.fields["game_headline"].initial = headline
            form.fields["game_body"].initial = body
            form.fields["home_team"].initial = home_details.get("team")
            form.fields["home_hits"].initial = home_details.get("hits")
            form.fields["home_runs"].initial = home_details.get("runs")
            form.fields["home_errors"].initial = home_details.get("errors")
            form.fields["away_team"].initial = away_details.get("team")
            form.fields["away_hits"].initial = away_details.get("hits")
            form.fields["away_runs"].initial = away_details.get("runs")
            form.fields["away_errors"].initial = away_details.get("errors")
            form.fields["game_datetime"].initial = game_date
            form.fields["game_id"].initial = game_id
            form.fields["venue_id"].initial = get_venue_id(game_id, 1)
        except:
            pass

        context = {
            "form": form,
            "teams": teams,
            "games": display_dates,
            "test": request.GET,
            "pages": {"header": "Add a Game"},
            "default_values": default_values,
            "leagues": leagues,
            'request': request,
        }
        return render(request, "stadium_tracker/gamedetails_form.html", context)

    def form_valid(self, form):
        form.instance.user = self.request.user
        try:
            return super().form_valid(form)
        except IntegrityError:
            display_dates = get_form_details(self.request)
            game_id = display_dates[0].get("gamePk")
            home_details = get_boxscore(game_id, "home")
            away_details = get_boxscore(game_id, "away")
            game_date = get_game_date(game_id, 1)
            game_date = game_date.date().strftime("%m/%d/%Y")
            teams = get_teams(1)
            home_team = home_details.get("team")
            away_team = away_details.get("team")
            text = f"{home_team} vs {away_team} on {game_date}"
            user = self.request.user
            user = str(user).title()
            error = f"The game has already been added for user {user} <br> {text}"
            context = {
                "teams": teams,
                "pages": {"header": "Add a Game"},
                "error": error,
            }
            return render(
                self.request, "stadium_tracker/gamedetails_form.html", context=context
            )


class GameDetailDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = GameDetails
    context_object_name = "game_details"
    success_url = reverse_lazy("stadium_tracker:my_game_list")

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class VenueList(ListView):
    model = GameDetails
    context_object_name = 'games'
    template_name = "stadium_tracker/venue_list.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["default_division"] = 203
        data["divisions"] = Division.objects.filter(sport_id=Sport.objects.filter(name='Major League Baseball').first()).order_by('name')
        data["teams"] = Team.objects.filter(sport_id=Sport.objects.filter(name='Major League Baseball').first())
        data["stadium"] = GameDetails.objects.order_by().values_list('stadium', flat=True).distinct()
        return data


class MyVenues(LoginRequiredMixin, VenueList):
    template_name = "stadium_tracker/my_venue_list.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["default_division"] = 203
        data["pages"] = {"header": "My Visited Stadia"}
        data["stadium"] = data['stadium'].filter(user=1)
        return data
