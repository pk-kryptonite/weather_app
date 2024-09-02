from django.db import models

class WeatherCache(models.Model):
    file_name = models.CharField(max_length=255, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
