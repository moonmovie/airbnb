from django.db import models

# python import-django - 외부패키지 extenal pakage - application,inside pakage 순으로 하기
from django_countries.fields import CountryField
from core import models as core_models

# from users import models as user_models

# Create your models here.


class AbstractItem(core_models.TimeStampedmodel):

    # Abstract Model

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """ RoomType Object Definition """

    class Meta:
        verbose_name = "Room type"


class Amenity(AbstractItem):

    """ Amenity Object Definition """

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """ Facility Model Definition """

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """ HouseRule Model Definition """

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedmodel):
    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    rooom = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedmodel):
    name = models.CharField(max_length=140, null=False, default="")
    description = models.TextField(null=True)
    country = CountryField(null=True)
    city = models.CharField(max_length=80, default="")
    price = models.IntegerField(null=True)
    address = models.CharField(max_length=140, default="")
    guests = models.IntegerField(null=True)
    beds = models.IntegerField(null=True)
    bedsrooms = models.IntegerField(null=True)
    baths = models.IntegerField(null=True)
    check_in = models.TimeField(null=True)
    check_out = models.TimeField(null=True)
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey("users.User", on_delete=models.CASCADE, default="")
    room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField("Amenity", blank=True)
    facility = models.ManyToManyField("Facility", blank=True)
    houserule = models.ManyToManyField("HouseRule", blank=True)

    def __str__(self):
        return self.name
