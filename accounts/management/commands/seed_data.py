from django.core.management.base import BaseCommand
from accounts.models import User
from events.models import Event
from positions.models import Position
from django.utils import timezone
from datetime import timedelta


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        # ❗ DELETE OLD DATA
        User.objects.all().delete()
        Event.objects.all().delete()
        Position.objects.all().delete()

        # ✅ ALL REQUIRED POSITIONS
        positions_list = [
            'Security', 'Greeter', 'Cook',
            'Swamper', 'Setup', 'Tear Down', 'Server'
        ]

        for p in positions_list:
            Position.objects.create(name=p)

        # ✅ ADMIN
        User.objects.create_user(
            username='admin@a.ca',
            email='admin@a.ca',
            password='Pa55worD',
            role='admin'
        )

        # ✅ MEMBERS
        User.objects.create_user(
            username='a@b.ca',
            email='a@b.ca',
            password='Pa55worD',
            role='member'
        )

        User.objects.create_user(
            username='b@b.ca',
            email='b@b.ca',
            password='Pa55worD',
            role='member'
        )

        # ✅ VOLUNTEERS
        User.objects.create_user(
            username='vol1@b.ca',
            email='vol1@b.ca',
            password='Pa55worD',
            role='volunteer'
        )

        User.objects.create_user(
            username='vol2@b.ca',
            email='vol2@b.ca',

            password='Pa55worD',
            role='volunteer'
        )

        now = timezone.now()

        Event.objects.create(
            name='Past Event',
            description='This event has already happened.',
            start_date=now - timedelta(days=5),
            end_date=now - timedelta(days=3),
        )

        Event.objects.create(
            name='Current Event',
            description='This event is happening right now.',
            start_date=now - timedelta(days=1),
            end_date=now + timedelta(days=1),
        )

        Event.objects.create(
            name='Today Event',
            description='This event starts later today.',
            start_date=now + timedelta(hours=3),
            end_date=now + timedelta(hours=6),
        )

        Event.objects.create(
            name='Future Event 1',
            description='This event is coming up in 3 days.',
            start_date=now + timedelta(days=3),
            end_date=now + timedelta(days=4),
        )

        Event.objects.create(
            name='Future Event 2',
            description='This event is coming up in 6 days.',
            start_date=now + timedelta(days=6),
            end_date=now + timedelta(days=7),
        )

        self.stdout.write(self.style.SUCCESS('Done! Database seeded successfully.'))