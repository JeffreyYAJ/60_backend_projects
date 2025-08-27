from django.shortcuts import render
from django.http import JsonResponse
from .models import Score, Subject, Student
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def add_student(request):
    if request.method == "POST":
        data = json.loads(request.body)
        student = Student.objects.create(name = data['name'])
        return JsonResponse({"id": student.id, "Name": student.name})
    return JsonResponse({"Error": "POST method required"}) 
        
def list_student(request):
    students = list(Student.objects.values())
    return JsonResponse({"Students": students})
    
@csrf_exempt
def delete_student(request, id):
    try: 
        student = Student.objects.get(pk= id)
        student.delete()
        return JsonResponse({"Message": f"Student {student.name} deleted"})
    
    except Student.DoesNotExist:
        return JsonResponse({"Error": "Student not existing"})
    
    
@csrf_exempt
def add_subject(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        subject = Subject(name= data['name'])
        return JsonResponse({"id": subject.id, "Name":subject.name})
    return JsonResponse({"Error":"POST method required"})

def list_subjects(request):
    subjects = list(Subject.objects.values())
    return JsonResponse({"Subjects":subjects})

@csrf_exempt
def delete_subject(request, id):
    try:
        subject = Subject.objects.get(pk = id)
        subject.delete()
        return JsonResponse({"Message": "Subject Deleted"})
    except Subject.DoesNotExist:
        return JsonResponse({"Error": "Subject not existing"})
    

@csrf_exempt
def add_grade(request):
    if request.method == "POST":
        data = json.loads(request.body)
        try:
            student = Student.objects.get(pk= data['student_id'])
            subject = Subject.objects.get(pk = data['subject_id'])
            grade = Score.objects.create(student = student, subject= subject, score = float(data['score']))
            return JsonResponse({"id": grade.id, "student": student.name, "subject": subject.name, "score":grade.score})        
        
        except (Student.DoesNotExist, Subject.DoesNotExist):
            return JsonResponse({"Error":"Student or Subject not valid"})
        
def list_grade(request, student_id):
    grades = Score.objects.filter(student__id = student_id).select_related('subject')
    result = [ 
        {'subject': grade.subject.name, 'score': grade.score}
        for grade in grades
    ]
    
    return JsonResponse({'grades': result})

def average_student(request, student_id):
    grades = Score.objects.filter(student__id=student_id)
    if not grades.exists():
        return JsonResponse({'average': None, 'message': 'No grades for student'})
    avg = round(sum(g.score for g in grades) / grades.count(), 2)
    return JsonResponse({'average': avg})