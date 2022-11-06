from django.contrib import admin
from .models import Kit


@admin.register(Kit)
class KitAdminModel(admin.ModelAdmin):
    list_display = ('type', )
