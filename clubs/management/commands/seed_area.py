from django.core.management.base import BaseCommand

from clubs.models import Area

Name = "Areas"


# python manage.py seed_area
class Command(BaseCommand):

    help = f"This command creates many {Name}"

    def handle(self, *args, **options):
        areas = [
            "서대문구",
            "송파구",
            "그 외 지역",
        ]

        for a in areas:
            if Area.objects.filter(name=a):
                self.stdout.write(
                    self.style.WARNING(f"{len(areas)} {Name} already exist!")
                )
                return
            else:
                Area.objects.create(name=a)

        self.stdout.write(self.style.SUCCESS(f"{len(areas)} {Name} created!"))
