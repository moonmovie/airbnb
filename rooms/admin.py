from django.contrib import admin
from . import models
from django.utils.html import mark_safe

# Register your models here.

# admin + 추가 할수 있는 기능
@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin Definition """

    list_display = ("name", "used_by")

    def used_by(self, object):
        return object.rooms.count()


class PhototoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    inlines = (PhototoInline,)

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "city",
             "address", "price", "room_type",)},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Space", {"fields": ("guests", "beds", "bedsrooms", "baths")}),
        (
            "More About the Space",
            {
                "classes": ("collapse",),  # when page is a lot of stuff, show and hide
                "fields": ("amenities", "facility", "houserule"),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedsrooms",
        "baths",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    ordering = ("name", "price")

    list_filter = (
        "instant_book",
        "host__superhost",
        "host__gender",
        "room_type",
        "amenities",
        "facility",
        "houserule",
        "city",
        "country",
    )

    raw_id_fields = ("host",)

    # "city" is icontatins. we can search busan just from including "san".
    # "^city" is startswith. The value must be word for serarch item.

    search_fields = ("=city", "^host__username")

    filter_horizontal = ("amenities", "facility", "houserule")

    # self is RoomAdmin , object is row
    # can not click here. just funtion. not sorting
    def count_amenities(self, object):
        return object.amenities.count()

    count_amenities.short_description = "happy"

    def count_photos(self, object):
        return object.photos.count()

    count_photos.short_description = "Photo Count"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition"""

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, object):

        return mark_safe(f'<img width="5%" src = "{object.file.url}"/>')

    get_thumbnail.short_description = "thumbnail"
    
    