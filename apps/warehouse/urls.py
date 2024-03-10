from django.urls import path, include
#Project
from apps.warehouse.views import ProductStatisticsView

urlpatterns = [
    path('statistics/', ProductStatisticsView.as_view()),
]