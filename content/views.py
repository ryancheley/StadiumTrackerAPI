# TODO: convert Home Page from TemplateView to DetailView
from datetime import datetime
from django.views.generic import DetailView, RedirectView
from content.models import Content
from stadium_tracker.models import GameDetails
from stadium_tracker.game_details import get_games_for_date


class ContentRedirectView(RedirectView):
    permanent = True
    query_string = True
    pattern_name = "home"


class ContentDetailView(DetailView):
    model = Content
    template_name = "page.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    context_object_name = "pages"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["games"] = GameDetails.objects.all().order_by("-create_date")[:3]
        data["today"] = get_games_for_date(
            1, datetime.strftime(datetime.now(), "%Y-%m-%d")
        )
        return data
