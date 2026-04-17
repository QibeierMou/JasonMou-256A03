from django.test import TestCase
from django.urls import reverse
from accounts.models import User
from events.models import Event
from django.utils import timezone
from datetime import timedelta

# Create your tests here.
class ReportsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email="admin@test.com",
            username="admin",
            password="test1234",
            role="admin"
        )

        self.client.login(email="admin@test.com", password="test1234")

    def test_upcoming_events_view(self):
        Event.objects.create(
            name="Future Event",
            description="Test",
            start_date=timezone.now() + timedelta(days=1),
            end_date=timezone.now() + timedelta(days=2)
        )

        response = self.client.get(reverse('upcoming_events'))
        self.assertEqual(response.status_code, 200)

    def test_all_events_view(self):
        response = self.client.get(reverse('all_events'))
        self.assertEqual(response.status_code, 200)

    def test_user_list_view(self):
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, 200)