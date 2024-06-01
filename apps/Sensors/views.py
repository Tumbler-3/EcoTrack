from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from apps.Sensors.models import Sensor
from apps.Sensors.serializers import SensorSerializer
from rest_framework.pagination import PageNumberPagination
from apps.User.permissions import IsAdmin
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.utils.decorators import method_decorator
from django.core.cache import cache


class SensorViewAPI(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAdmin,]
    
    @method_decorator(cache_page(60*10))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        cache.clear()
        return self.create(request, *args, **kwargs)


class SensorDetailViewAPI(RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    lookup_field = 'id'
    permission_classes = [IsAdmin,]
    
    @method_decorator(cache_page(60*10))
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
    
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        cache.clear()
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        cache.clear()
        return self.destroy(request, *args, **kwargs)