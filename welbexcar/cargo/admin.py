from django.contrib import admin
from .models import Car, Cargo, Location


class LocationAdmin(admin.ModelAdmin):
    list_display = ('city')


admin.site.register(Car)
admin.site.register(Cargo)
admin.site.register(Location)