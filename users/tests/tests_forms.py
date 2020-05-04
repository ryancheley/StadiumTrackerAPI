from django.test import TestCase
from users.forms import CustomUserChangeForm


class CustomUserChangeFormTest(TestCase):

    def test_valid_data(self):
        form = CustomUserChangeForm({
            'username': "TurangaLeela",
            'email': "leela@example.com",
            'favorite_team': 119,
            'password': 'abc123++'

        })
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertEqual(user.username, "TurangaLeela")
        self.assertEqual(user.email, "leela@example.com")
        self.assertEqual(user.favorite_team, 119)

    def test_blank_data(self):
        form = CustomUserChangeForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'username': ['This field is required.'],
        })
