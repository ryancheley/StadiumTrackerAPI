# TODO: convert Home Page from TemplateView to DetailView
from datetime import datetime
from django.views.generic import DetailView, RedirectView
from content.models import Content


class ContentRedirectView(RedirectView):
    permanent = True
    query_string = True
    pattern_name = 'home'


class ContentDetailView(DetailView):
    model = Content
    template_name = 'page.html'
    slug_field = 'title'
    slug_url_kwarg = 'title'
    context_object_name = 'pages'
