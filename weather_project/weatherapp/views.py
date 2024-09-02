from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
import os
from datetime import datetime, timedelta
from django.conf import settings
from .models import WeatherCache


from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')
CACHE_DIR = 'cache/' 
CACHE_EXPIRY = timedelta(minutes=180)  

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')

def weather(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        lat = float(data['lat'])
        lon = float(data['lon'])
        city_name = data.get('city_name', f"{lat}-{lon}")
        file_name = f"{city_name}.txt"
        file_path = os.path.join(CACHE_DIR, file_name)
        current_time = datetime.now()

        # Check if cache file exists and is valid
        try:
            cache_entry = WeatherCache.objects.get(file_name=file_name)
            cache_age = current_time - cache_entry.timestamp
            if cache_age < CACHE_EXPIRY and os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    cached_data = json.load(file)
                return HttpResponse(json.dumps(cached_data), content_type='application/json')
        except WeatherCache.DoesNotExist:
            pass

     
        url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units=metric&exclude=hourly,daily&appid={API_KEY}"
        result = requests.get(url)
        response = result.json()
        temp = response['current']['temp']

    
        if not os.path.exists(CACHE_DIR):
            os.makedirs(CACHE_DIR)
        with open(file_path, 'w') as file:
            json.dump({'temperature': temp}, file)
        
       
        WeatherCache.objects.update_or_create(
            file_name=file_name,
            defaults={'timestamp': current_time}
        )

        context = {'temperature': temp}
        return HttpResponse(json.dumps(context), content_type='application/json')

def geoapi(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        city_name = data['city_name']
        url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={API_KEY}"
        response = requests.get(url)
        result = response.json()
        return HttpResponse(json.dumps(result), content_type='application/json')
