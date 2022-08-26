from django.http import Http404
from django.shortcuts import render
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404

# Create your views here.


def home(request):
    projects = Projects.get_projects()
    return render (request, 'index.html',{'projects':projects})

def get_projects(request, id):
    try:
        project = Projects.objects.get(pk=id)
    except ObjectDoesNotExist:
        raise Http404()
    
    return render (request, 'project.html', {'project':project})