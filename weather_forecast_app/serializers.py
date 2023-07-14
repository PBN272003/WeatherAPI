from rest_framework import serializers
from .models import WeatherData
class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = ['latitude', 'longitude', 'detailing_type', 'forecast_data', 'last_updated']
