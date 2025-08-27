from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import Victim
import requests

@csrf_exempt
def tracker(request):
    if request.method == "POST":
        data = json.loads(request.body)
        ip = data['ip']
        
        if not ip:
            return JsonResponse({"Error": "No IP provided"})
        
        response  = requests.get(f"https://ipapi.co/{ip}/json")
        if response.status_code != 200:
            return JsonResponse({"Error":"Failed to get Location"})
        
        info = response.json()
        victim_location = Victim.objects.create(ip_address = ip, city = info.get('city'), region = info.get('region'), longitude = info.get('longitude'), latitude = info.get('latitude'), country = info.get('country_name'))
        
        return JsonResponse({
            'ip': victim_location.ip_address,
            'city': victim_location.city,
            'region': victim_location.region,
            'country': victim_location.country,
            'latitude': victim_location.latitude,
            'longitude': victim_location.longitude
        })
        
def list_ips(request):
    ips = list(Victim.objects.values())
    index = 1
    victim_dict= []
    for ip  in ips:
        victim_dict.append(f"victim{index}: {ip}")
    
    return JsonResponse({"victims":ips})
    
