from django.urls import path
from . import views

urlpatterns = [
    path('tracker', views.tracker),
    path('list_victims' , views.list_ips)
]
