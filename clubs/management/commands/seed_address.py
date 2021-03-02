import os
import random

from django.core.management.base import BaseCommand
from django_seed import Seed

from clubs.models import Address, Area, Town

os.system("python manage.py seed_area")
os.system("python manage.py seed_town")

Name = "Addresses"


# python manage.py seed_address --number 10
class Command(BaseCommand):

    help = f"This command creates many {Name}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help=f"How many {Name} do you want to create?",
        )

    def handle(self, *args, **options):
        # addresses = [
        #     "신총동 신촌 기찻길",
        #     "송파구",
        #     "그 외 지역",
        # ]

        number = options.get("number", 1)
        seeder = Seed.seeder()
        areas = Area.objects.all()
        towns = Town.objects.all()

        seeder.add_entity(
            Address,
            number,
            {
                # "name": lambda x: random.choice(addresses),
                "name": lambda x: seeder.faker.street_address(),
                "area": lambda x: random.choice(areas),
                "town": lambda x: random.choice(towns),
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} {Name} created!"))
