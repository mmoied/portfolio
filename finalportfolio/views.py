from django.shortcuts import render
from .models import Projects

def index(request):
    return render(request, 'finalportfolio/index.html', {}) 

def work(request):
    return render(request, 'finalportfolio/work.html', {}) 

def projects(request):
    work1 = Projects.objects.order_by('-start')
    return render(request, 'finalportfolio/projects.html', {'projects':work1})
