from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'finalportfolio/index.html', {}) 

def work(request):
    return render(request, 'finalportfolio/work.html', {}) 
