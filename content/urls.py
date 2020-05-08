from django.urls import path
from content.views import ContentTemplateView, ContentDetailView

app_name = 'content'


urlpatterns = [
    path('', ContentTemplateView.as_view(template_name='page.html'), name='home'),
    path('Pages/<slug:title>', ContentDetailView.as_view(template_name='page.html'), name='content_detail'),
]
