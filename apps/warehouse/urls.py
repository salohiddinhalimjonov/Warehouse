from django.urls import path, include
from apps.warehouse.views import ProductStatisticsView

urlpatterns = [
    path('statistics/', ProductStatisticsView.as_view()),
]