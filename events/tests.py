from django.test import TestCase

# Create your tests here.
from .models import Event

class EventTest(TestCase):

    def test_create_event(self):
        event = Event.objects.create(
            name="Test Event",
            description="Test",
            start_date="2026-04-20",
            end_date="2026-04-21"
        )
        self.assertEqual(event.name, "Test Event")