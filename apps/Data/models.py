from django.db import models
from apps.Sensors.models import Sensor



class Data(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='sensor_data')
    PM2_5 = models.FloatField()
    PM10 = models.FloatField()
    CO2 = models.FloatField()
    timestamp = models.DateField()
    
    def __str__(self):
        return f'{self.sensor.model} data'

    class Meta:
        verbose_name = 'Data',
        verbose_name_plural = 'Data'