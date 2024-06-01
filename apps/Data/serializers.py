from rest_framework import serializers
from apps.Data.models import Data


class DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = '__all__'
        
    sensor_name = serializers.SerializerMethodField()
    
    def get_sensor_name(self, obj):
        return f'{obj.sensor.model}'