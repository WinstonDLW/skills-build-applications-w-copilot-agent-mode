from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import connection
from octofit_tracker import models

from djongo import models as djongo_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear all collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        # Create Users
        users = [
            User(email='ironman@marvel.com', username='ironman', team=marvel),
            User(email='captainamerica@marvel.com', username='captainamerica', team=marvel),
            User(email='batman@dc.com', username='batman', team=dc),
            User(email='superman@dc.com', username='superman', team=dc),
        ]
        for user in users:
            user.set_password('password123')
            user.save()

        # Create Activities
        activities = [
            Activity(user=users[0], type='run', duration=30, distance=5),
            Activity(user=users[1], type='cycle', duration=45, distance=20),
            Activity(user=users[2], type='swim', duration=60, distance=2),
            Activity(user=users[3], type='run', duration=25, distance=4),
        ]
        for activity in activities:
            activity.save()

        # Create Workouts
        workouts = [
            Workout(name='Morning Cardio', description='A quick morning run.'),
            Workout(name='Strength Training', description='Upper body workout.'),
        ]
        for workout in workouts:
            workout.save()

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        # Ensure unique index on email
        with connection.cursor() as cursor:
            cursor.execute('db.users.createIndex({ "email": 1 }, { "unique": true })')

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))

# Models must be defined in octofit_tracker/models.py:
# Team, Activity, Leaderboard, Workout
