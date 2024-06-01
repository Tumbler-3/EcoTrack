# Generated by Django 5.0 on 2024-06-01 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=70)),
                ('eq_type', models.CharField(max_length=70)),
                ('inst_date', models.DateField()),
                ('status', models.CharField(max_length=70)),
            ],
            options={
                'verbose_name': ('Sensor',),
                'verbose_name_plural': 'Sensors',
            },
        ),
    ]
