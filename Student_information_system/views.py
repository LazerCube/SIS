from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic

from .models import tblStudent

def index(request):
    return HttpResponse('Index')

def students(request, student_id):
    student = get_object_or_404(tblStudent, pk=student_id)
    context = {
        'student': student,
    }
    return render(request, 'SIS/index.html', context)

def classes(request):
    return HttpResponse('Classes!')

def units(request):
    return HttpResponse('Units')
