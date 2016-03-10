from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def index(request):
    return HttpResponseRedirect(reverse('SIS:index'))

def page_not_found(request):
    msg = "Page Not Found."
    context = {
        'error_code': 404,
        'error_msg': msg,
    }
    return render(request, 'error.html', context)

def server_error(request):
    msg = "Server Error."
    context = {
        'error_code': 500,
        'error_msg': msg,
    }
    return render(request, 'error.html', context)
