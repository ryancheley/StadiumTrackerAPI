from django.urls import path
from content.views import ContentRedirectView, ContentDetailView

app_name = "content"


urlpatterns = [
    path("", ContentRedirectView.as_view(url="Pages/Home"), name="home"),
    path(
        "Pages/<slug:slug>",
        ContentDetailView.as_view(template_name="page.html"),
        name="content_detail",
    ),
]
