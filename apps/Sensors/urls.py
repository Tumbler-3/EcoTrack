from django.urls import path
from apps.Sensors.views import SensorDetailViewAPI, SensorViewAPI


urlpatterns = [
    path('', SensorViewAPI.as_view()),
    path('<int:id>/', SensorDetailViewAPI.as_view()),
]