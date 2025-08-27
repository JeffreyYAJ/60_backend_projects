from django.urls import path
from .views import protected_view



urlpatterns = [
    path('api/protected/', protected_view, name='protected'),
]