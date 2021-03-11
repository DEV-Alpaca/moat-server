import random

from django.core.management.base import BaseCommand
from django_seed import Seed

from apps.clubs import models as club_models
from apps.users import models as user_models

Name = "Clubs"


# python manage.py seed_club --number 10
class Command(BaseCommand):

    help = f"This command creates many {Name}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help=f"How many {Name} do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number", 2)
        seeder = Seed.seeder()
        all_user = user_models.User.objects.all()
        club_types = club_models.ClubType.objects.all()
        addresses = club_models.Address.objects.all()
        seeder.add_entity(
            club_models.Club,
            number,
            {
                "host": lambda x: random.choice(all_user),
                "club_type": lambda x: random.choice(club_types),
                "address": lambda x: random.choice(addresses),
                "name": lambda x: seeder.faker.bs(),
                "cost": lambda x: random.randint(1, 300) * 1000,
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} {Name} created!"))
