from django.contrib import admin
from .models import StationAdmin

# Register your models here.
@admin.register(StationAdmin)
class StationAdminAdmin(admin.ModelAdmin):
    list_display = ['name', 'number', 'email',]
