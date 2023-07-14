from django.db import models
from django.utils import timezone

# Create your models here.
class WeatherData(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    detailing_type_choices = (
        ('current','current weather'),
        ('hourly','Hourly forecast'),
        ('daily','Daily forecast'),
    )
    detailing_type = models.CharField(max_length=1000,choices=detailing_type_choices)
    forecast_data = models.JSONField()
    last_updated = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Weather Data id:{self.pk}"