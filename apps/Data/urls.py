from django.urls import path
from apps.Data.views import DataViewAPI, DataDetailViewAPI


urlpatterns = [
    path('', DataViewAPI.as_view()),
    path('<int:id>/', DataDetailViewAPI.as_view()),
]