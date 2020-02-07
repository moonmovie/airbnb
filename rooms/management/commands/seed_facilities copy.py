from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):

    help = "this command creates facilities"

    def handle(self, *args, **options):

        facilities = [
            "Self check-in",
            "Free parking on premises",
            "Elevator" "Gym",
            "Hot tub",
            "Pool",
        ]

        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS("facilities created!"))

