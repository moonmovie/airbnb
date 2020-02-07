from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):

    help = "this command creates amenities"

    # def add_arguments(self, parser):
    #     parser.add_argument("--times", help="happyday")

    def handle(self, *args, **options):
        """
        The actual logic of the command. Subclasses must implement
        this method.
        """
        # print(args, options)
        # times = options.get("times")
        # for t in range(0, int(times)):
        #     # print("yes")
        #     self.stdout.write(self.style.SUCCESS("LOVE YOU"))
        amenities = [
            "Kitchen",
            "Shampoo",
            "Heating",
            "Air conditioning",
            "Wifi",
            "Hangers",
            "Iron",
            "Hair dryer",
            "Laptop-friendly workspace",
            "TV",
            "Private bathroom",
            "Washer",
            "Dryer",
            "Breakfast",
            "Indoor fireplace",
            "Crib",
            "High chair",
        ]

        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Anebities created!"))

