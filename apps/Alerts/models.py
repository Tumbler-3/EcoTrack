from django.db import models
from apps.Sensors.models import Sensor


class Alerts(models.Model):
    choices = {'Low': 'Low', 'Medium': 'Medium', 'High': 'High'}

    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='sensor_alerts')
    polution_level = models.CharField(choices=choices, max_length=10)
    desc = models.TextField(null=True, blank=True)
    alert_time = models.TimeField()
    
    def __str__(self):
        return f'{self.sensor.model} alert'

    class Meta:
        verbose_name = 'Alert',
        verbose_name_plural = 'Alerts'
