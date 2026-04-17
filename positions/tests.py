from django.test import TestCase
from .models import Position

# Create your tests here.
class PositionTest(TestCase):

    def test_create_position(self):
        position = Position.objects.create(name="Manager")

        self.assertEqual(position.name, "Manager")

    def test_position_list(self):
        Position.objects.create(name="Helper")
        Position.objects.create(name="Leader")

        positions = Position.objects.all()

        self.assertEqual(positions.count(), 2)