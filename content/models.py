from django.db import models
from StadiumTrackerAPI import settings
from django.urls import reverse

# Be sure to add a test to tests_models BEFORE adding new attributes to these models


class Content(models.Model):
    title = models.TextField()
    page_content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('content_detail', kwargs={'slug': self.slug})
