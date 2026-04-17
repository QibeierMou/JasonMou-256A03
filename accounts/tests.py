from django.test import TestCase
from .models import User

# Create your tests here.
class UserModelTest(TestCase):

    def test_create_user(self):
        user = User.objects.create_user(
            email="test@example.com",
            username="testuser",
            password="test1234",
            role="member"
        )

        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.role, "member")
        self.assertTrue(user.check_password("test1234"))