from django.contrib import admin
from .models import Drug


@admin.register(Drug)
class DrugAdminModel(admin.ModelAdmin):
    list_display = ('type', )
