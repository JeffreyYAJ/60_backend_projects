from django.urls import path
from .views import verify_email, register

urlpatterns = [
    path('register', register),
    path('verify/<uuid:token>/', verify_email)
]
