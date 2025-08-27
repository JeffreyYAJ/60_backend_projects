from django.urls import path
from .views import convert_yen_euro, convert_euro_yen

urlpatterns = [
    path('convert_yen_euro', convert_yen_euro),
    path('convert_euro_yen', convert_euro_yen),

]
