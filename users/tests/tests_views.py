from django.test import TestCase
from django.urls import reverse

from users.models import CustomUser


class UserUpdateViewTest(TestCase):

    def test_update_book(self):
        user = CustomUser.objects.create(username='test')

        response = self.client.post(
            reverse('users:user', kwargs={'pk': user.id}),
            {'username': 'test', })

        self.assertEqual(response.status_code, 302)

        user.refresh_from_db()
        self.assertEqual(user.username, 'test')
