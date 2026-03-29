from django.test import TestCase
from .models import Team, User, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(email='test@example.com', username='testuser', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='Test Desc')
        self.activity = Activity.objects.create(user=self.user, type='run', duration=10, distance=2.5)
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=50)

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Test Team')
    def test_user_email(self):
        self.assertEqual(self.user.email, 'test@example.com')
    def test_activity_type(self):
        self.assertEqual(self.activity.type, 'run')
    def test_workout_name(self):
        self.assertEqual(self.workout.name, 'Test Workout')
    def test_leaderboard_points(self):
        self.assertEqual(self.leaderboard.points, 50)
