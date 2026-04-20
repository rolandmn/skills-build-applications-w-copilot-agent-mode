from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from core.models import Team, Workout, Activity, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Verwijder bestaande data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        # Users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='test', team=marvel),
            User.objects.create_user(username='captain', email='captain@marvel.com', password='test', team=marvel),
            User.objects.create_user(username='batman', email='batman@dc.com', password='test', team=dc),
            User.objects.create_user(username='superman', email='superman@dc.com', password='test', team=dc),
        ]

        # Workouts
        workout1 = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        workout2 = Workout.objects.create(name='Running', description='Run 5km')

        # Activities
        Activity.objects.create(user=users[0], workout=workout1, duration=10, calories=50)
        Activity.objects.create(user=users[1], workout=workout2, duration=30, calories=200)
        Activity.objects.create(user=users[2], workout=workout1, duration=15, calories=70)
        Activity.objects.create(user=users[3], workout=workout2, duration=25, calories=180)

        # Leaderboard
        Leaderboard.objects.create(user=users[0], points=100)
        Leaderboard.objects.create(user=users[1], points=90)
        Leaderboard.objects.create(user=users[2], points=110)
        Leaderboard.objects.create(user=users[3], points=95)


        # Unieke index op email veld is al geregeld via het User model

        self.stdout.write(self.style.SUCCESS('octofit_db succesvol gevuld met testdata!'))


