import requests
from django.http import JsonResponse

API_KEY = 'TA_CLE_API_OPENWEATHERMAP'

def get_weather(request):
    city = request.GET.get('city')
    if not city:
        return JsonResponse({'error': 'city parameter is required'}, status=400)

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=fr'
    response = requests.get(url)

    if response.status_code != 200:
        return JsonResponse({'error': 'City not found or API error'}, status=response.status_code)

    data = response.json()
    return JsonResponse({
        'city': city,
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed']
    })
