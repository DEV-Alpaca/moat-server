from django.core.management.base import BaseCommand

from clubs.models import Town

Name = "Towns"


# python manage.py seed_town
class Command(BaseCommand):

    help = f"This command creates many {Name}"

    def handle(self, *args, **options):
        towns = [
            "홍제동",
            "신촌동",
            "그 외 지역",
        ]

        for t in towns:
            if Town.objects.filter(name=t):
                self.stdout.write(
                    self.style.WARNING(f"{len(towns)} {Name} already exist!")
                )
                return
            else:
                Town.objects.create(name=t)

        self.stdout.write(self.style.SUCCESS(f"{len(towns)} {Name} created!"))
