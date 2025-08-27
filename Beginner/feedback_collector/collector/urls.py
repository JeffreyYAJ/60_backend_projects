from django.urls import path
from .views import test, send_feedback

urlpatterns = [
    path('test/', test),
    path('feedback', send_feedback)
]
