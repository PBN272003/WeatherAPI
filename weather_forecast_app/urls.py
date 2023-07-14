from django.urls import path
from .views import location_input, weather_data

urlpatterns = [
    path('location-input/',location_input,name='location-input'),
    path('weather-data/<str:lat>/<str:lon>/<str:detailing_type>/',weather_data,name='weather-data'),
]
