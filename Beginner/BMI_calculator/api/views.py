from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def calculate(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            weight = float(data['weight'])
            height = float(data['height'])
            
            bmi = weight / height**2
            category = "obese"
            
            if bmi < 30:
                category = 'Overweight'
            if bmi < 25:
                category = 'Normal weight'
            if bmi < 15:
                category = 'Underweight'
                
            return JsonResponse({"BMI":bmi, "Category":category})
            
        except( KeyError, ValueError):
            JsonResponse({"Error":"Unexpected value"})