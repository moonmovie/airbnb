from django.contrib import admin
from . import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    """ Review Admin Difinition """

    list_display = ("__str__", "roomname", "rating_average")

