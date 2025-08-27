from .views import calculate
from django.urls import path

urlpatterns = [
    path('bmi', calculate)
]
