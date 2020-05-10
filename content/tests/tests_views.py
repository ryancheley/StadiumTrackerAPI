from django.test import TestCase, override_settings
from content.models import Content
from users.models import CustomUser


def create_user(username):
    return CustomUser.objects.create(username=username)


def create_content(title, content, slug):
    author = create_user('ryan')
    return Content.objects.create(title=title, page_content=content, author=author, slug=slug)


class ContentTemplateViewTests(TestCase):

    def test_page_content(self):
        page = create_content('Test', 'Test Page Content', 'Test')
        self.assertEqual(page.title, 'Test')
        self.assertEqual(page.page_content, 'Test Page Content')

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_page_exists(self):
        page = create_content('Test', 'Test Page Content', 'Test')
        response = self.client.get(f'/Pages/{page.slug}')
        self.assertEqual(response.status_code, 200)

    @override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
    def test_page_does_not_exist(self):
        page = create_content('Test', 'Test Page Content', 'Test')
        response = self.client.get(f'/{page.slug}')
        self.assertEqual(response.status_code, 404)

