from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(username='tony_stark', email='tony@avengers.com', password='ironman123'),
            User(username='steve_rogers', email='steve@avengers.com', password='shield456'),
            User(username='natasha_romanoff', email='natasha@avengers.com', password='blackwidow789'),
            User(username='bruce_wayne', email='bruce@dcheroes.com', password='batman101'),
            User(username='clark_kent', email='clark@dcheroes.com', password='superman202'),
        ]
        for user in users:
            user.save()
        self.stdout.write(self.style.SUCCESS('Users created successfully'))

        # Create teams
        team_marvel = Team(name='Team Marvel', members=['tony_stark', 'steve_rogers', 'natasha_romanoff'])
        team_marvel.save()
        team_dc = Team(name='Team DC', members=['bruce_wayne', 'clark_kent'])
        team_dc.save()
        self.stdout.write(self.style.SUCCESS('Teams created successfully'))

        # Create activities
        activities = [
            Activity(
                name='Running',
                description='Cardio running activity for improving stamina and endurance.',
                duration_minutes=30,
                schedule='Mondays at 6am',
                max_attendance=20,
            ),
            Activity(
                name='Walking',
                description='Low-impact walking activity suitable for all fitness levels.',
                duration_minutes=45,
                schedule='Wednesdays at 8am',
                max_attendance=25,
            ),
            Activity(
                name='Strength Training',
                description='Build muscle and improve overall body strength with resistance exercises.',
                duration_minutes=60,
                schedule='Thursdays at 5pm',
                max_attendance=10,
            ),
            Activity(
                name='Yoga',
                description='Improve flexibility, balance, and mental wellness through yoga practice.',
                duration_minutes=45,
                schedule='Fridays at 7am',
                max_attendance=15,
            ),
            Activity(
                name='Manga Maniacs',
                description='Explore the fantastic stories of the most interesting characters from Japanese Manga (graphic novels).',
                duration_minutes=90,
                schedule='Tuesdays at 7pm',
                max_attendance=15,
            ),
        ]
        for activity in activities:
            activity.save()
        self.stdout.write(self.style.SUCCESS('Activities created successfully'))

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(user='tony_stark', score=150),
            Leaderboard(user='steve_rogers', score=200),
            Leaderboard(user='natasha_romanoff', score=175),
            Leaderboard(user='bruce_wayne', score=225),
            Leaderboard(user='clark_kent', score=300),
        ]
        for entry in leaderboard_entries:
            entry.save()
        self.stdout.write(self.style.SUCCESS('Leaderboard entries created successfully'))

        # Create workouts
        workouts = [
            Workout(name='Morning Run', description='5km morning run to start the day energized.', duration_minutes=30),
            Workout(name='Evening Walk', description='Relaxing evening walk for recovery and stress relief.', duration_minutes=45),
            Workout(name='Power Lifting', description='Heavy lifting session focusing on compound movements.', duration_minutes=60),
        ]
        for workout in workouts:
            workout.save()
        self.stdout.write(self.style.SUCCESS('Workouts created successfully'))

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
