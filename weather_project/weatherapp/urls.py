from django.urls import path
from .views import index, geoapi, weather

urlpatterns = [
    path('', index, name= 'index'),
    path('geoapi', geoapi, name='geoapi'),
    path('weather', weather, name='weather'),
  
]


