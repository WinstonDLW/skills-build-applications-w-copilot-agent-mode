from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout


class ActivityModelTest(TestCase):
    def test_activity_creation(self):
        activity = Activity(
            name='Manga Maniacs',
            description='Explore the fantastic stories of the most interesting characters from Japanese Manga (graphic novels).',
            duration_minutes=60,
            schedule='Tuesdays at 7pm',
            max_attendance=15,
        )
        self.assertEqual(activity.name, 'Manga Maniacs')
        self.assertEqual(activity.description, 'Explore the fantastic stories of the most interesting characters from Japanese Manga (graphic novels).')
        self.assertEqual(activity.schedule, 'Tuesdays at 7pm')
        self.assertEqual(activity.max_attendance, 15)
