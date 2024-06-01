from django.db import models


class Sensor(models.Model):
    model = models.CharField(max_length=70)
    eq_type = models.CharField(max_length=70)
    inst_date = models.DateField()
    status = models.CharField(max_length=70)
    
    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Sensor',
        verbose_name_plural = 'Sensors'