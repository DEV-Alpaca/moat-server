from django.core.management.base import BaseCommand

from clubs.models import ClubType

Name = "ClubTypes"


# python manage.py seed_clubtype
class Command(BaseCommand):

    help = f"This command creates many {Name}"

    def handle(self, *args, **options):
        clubtypes = [
            "만나요",
            "전화/카톡",
        ]

        for c in clubtypes:
            if ClubType.objects.filter(name=c):
                self.stdout.write(
                    self.style.WARNING(f"{len(clubtypes)} {Name} already exist!")
                )
                return
            else:
                ClubType.objects.create(name=c)

        self.stdout.write(self.style.SUCCESS(f"{len(clubtypes)} {Name} created!"))
