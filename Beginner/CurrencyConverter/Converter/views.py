from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from .models import Conversions


@csrf_exempt
def convert_yen_euro(request):
    if request.method == "POST":
        data = json.loads(request.body)
        first_value = float(data['value'])

        converted_value = first_value * 0.005837
        conversion = Conversions.objects.create(value= first_value, converted = converted_value)

        return JsonResponse({f"{first_value}Y": f"{(converted_value)}€"})


@csrf_exempt
def convert_euro_yen(request):
    if request.method == "POST":
        data = json.loads(request.body)
        first_value = float(data['value'])

        converted_value = round(first_value/ 0.005837, 2)
        conversion = Conversions.objects.create(value = first_value, converted= converted_value)
        return JsonResponse({f"{first_value}€": f"{converted_value}Y"})




