from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic

from .models import tblStudent

class IndexView(generic.DetailView):
    model = tblStudent
    template_name = 'SIS/index.html'

class StudentView(generic.DetailView):
    model = tblStudent
    template_name = 'SIS/index.html'

def students(request):
    return HttpResponse('Student!')

def classes(request):
    return HttpResponse('Classes!')

def units(request):
    return HttpResponse('Units')
