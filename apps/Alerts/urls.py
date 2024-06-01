from django.urls import path
from apps.Alerts.views import AlertsViewAPI, AlertsDetailViewAPI


urlpatterns = [
    path('', AlertsViewAPI.as_view()),
    path('<int:id>/', AlertsDetailViewAPI.as_view()),
]