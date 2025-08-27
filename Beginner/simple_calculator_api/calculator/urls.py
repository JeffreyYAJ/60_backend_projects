from django.urls import path 
from .views import calculate, test

urlpatterns = [
    path('calculate', calculate),
    path('test', test)
]
