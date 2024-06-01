# Generated by Django 5.0 on 2024-06-01 04:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Sensors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alerts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polution_level', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], max_length=10)),
                ('desc', models.TextField(blank=True, null=True)),
                ('alert_time', models.TimeField()),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensor_alerts', to='Sensors.sensor')),
            ],
            options={
                'verbose_name': ('Alert',),
                'verbose_name_plural': 'Alerts',
            },
        ),
    ]
