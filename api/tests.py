from django.test import TestCase
from .models import UserProfile


class UserprofileModelTest(TestCase):
    """ Tests for the User profile Model """

    def test_can_save_a_user(self):
        UserProfile.objects.create(
            email="sectest2@gmail.com",
            password="devpassword2",
            name="NewPerson",
        )
        user_profile = UserProfile.objects.get(
            name="NewPerson"
        )

        self.assertEqual(UserProfile.objects.count(), 1)
        self.assertIn("sectest2@gmail.com", user_profile.email)