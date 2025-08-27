from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Feedback

def test(request):
    return HttpResponse("Feedback")

@csrf_exempt
def send_feedback(request):
    if request.method == "POST":
        data = json.loads(request.body)
        if 'comment' not in data:
            data['comment'] = ''
        feedback = Feedback.objects.create(username = data['username'], stars = data['stars'], comment = data['comment'])
        return JsonResponse({"Message":"Feedback created"})
        
        

        