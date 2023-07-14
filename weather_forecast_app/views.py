
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from .forms import LocationForm
from .models import WeatherData
from .serializers import WeatherDataSerializer
#from django.conf import settings

@api_view(['POST'])
def location_input(request):
    form = LocationForm(request.data)
    if form.is_valid():
        latitude = form.cleaned_data['latitude']
        longitude = form.cleaned_data['longitude']
        detailing_type = form.cleaned_data['detailing_type']
        processed_data = {
            'latitude':latitude,
            'longitude':longitude,
            'detailing_type':detailing_type,
            'message':'Form data processed successfully',
        }
        return Response(processed_data)

    return Response({'message': 'Invalid form data'}, status=400)


@api_view(['GET'])
def weather_data(request, lat, lon, detailing_type):
    valid_detailing_types = ['current', 'hourly', 'daily']
    if detailing_type not in valid_detailing_types:
        return Response({'error': 'Invalid detailing type'}, status=400)
    
    try:
        latitude = float(lat)
        longitude = float(lon)
    except ValueError:
        return Response({'error':'Invalid latitude or longitude'},status=400)
        

    weather_data = WeatherData.objects.filter(latitude=latitude, longitude=longitude, detailing_type=detailing_type).first()

    if weather_data is None:
        url = f"https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}&appid=884277fbe0daf4935521451396e7412f"
        response = requests.get(url)
        if response.status_code==200:
            forecast_data = response.json()
            print(f"Retrieved forecast data: {forecast_data}")
            weather_data = WeatherData(latitude = latitude, longitude = longitude, detailing_type = detailing_type, forecast_data =forecast_data)
            weather_data.save()
    
    
    serializer = WeatherDataSerializer(weather_data)
    print(f"Serialized data:{serializer.data}")
    return Response(serializer.data)
