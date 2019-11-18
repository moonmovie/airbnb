from django.contrib import admin
from . import models

# Register your models here.

# admin + 추가 할수 있는 기능
@admin.register(models.RoomType)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    pass
