from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

def add(num1, num2):
    return num1+ num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        return "Zero division error"


@csrf_exempt
def calculate(request):
    if request.method == 'POST':
        data = json.loads((request.body))
        
        number1 = float(data['num1'])
        number2 = float(data['num2'])
        operator = (data['operation'])
        
        if operator == '+':
            return JsonResponse({f"{number1}{operator}{number2}":add(number1, number2)})
        if operator == '-':
            return JsonResponse({f"{number1}{operator}{number2}":subtract(number1, number2)})
        if operator == '*':
            return JsonResponse({f"{number1}{operator}{number2}":multiply(number1, number2)})
        if operator == '/':
            return JsonResponse({f"{number1}{operator}{number2}":divide(number1, number2)})
        
        
        
def test():
    return json({"YO":"YO"})