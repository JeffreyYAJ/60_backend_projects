from django.shortcuts import render
from .models import Email
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        
        if Email.objects.filter(email=email).exists():
            return JsonResponse({"Error":"Email already exist"})
        
        user = Email.objects.create(email = email)
        
        verification_link = f"http://localhost:8000/api/verify/{user.verification_token}/"
        send_mail(
            'Verify your email',
            f'Click this link to verify: {verification_link}',
            'reply@yaj.com',
            [user.email],
            fail_silently=False,
        )
        
        return JsonResponse({"Message": "Verification link sent"})
    
def verify_email(request, token):
    user = get_object_or_404(Email, verification_token=token)
    user.is_verified = True
    user.save()
    
    return JsonResponse({"Message":"Email Enregistrer"})
    

    