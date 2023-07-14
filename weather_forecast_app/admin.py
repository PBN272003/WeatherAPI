from django.contrib import admin
from .models import WeatherData
# Register your models here.
@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'latitude', 'longitude', 'detailing_type', 'last_updated')