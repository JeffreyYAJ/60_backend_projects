from django.urls import path
from .views import get_quote

urlpatterns = [
    path('get_quote', get_quote),
]
