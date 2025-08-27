from django.shortcuts import render
from django.http import JsonResponse
import json
import requests
from django.views.decorators.csrf import csrf_exempt

def get_quote(request):
    data = (requests.get("https://api.quotable.io/random"))
    quote = data.json()
    
    return JsonResponse({"Author": quote.get('a') ,"Quote":quote.get('q')})