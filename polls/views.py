
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
# Create your views here.
from django.http import HttpResponse, Http404 ,HttpResponseRedirect
from .models import work,project, skills
from django.template import loader
from django.template.defaulttags import register

@register.filter
def get_range(value):
    return range(int(value))
@register.filter

def get_rangeq(value):
    return range(5-int(value))
# Create your tests here.
@register.filter
def split(value):
    return value.split('\n')
# Create your tests here.
def index(request):
    work1 = skills.objects.order_by('-level')
    return render(request, 'polls/index.html', {'skills':work1})
def project1(request):
    return render(request, 'polls/about.html', {})
def blog(request,id):
    work1 = project.object.get(pk=id)
    return render(request, 'polls/blog.html', {'project':work1})
def work1(request):
    work1 = work.objects.order_by('-end')
    return render(request, 'polls/collection.html', {'works':work1})
def services(request):
    return render(request, 'polls/services.html', {})
def single(request):
    return render(request, 'polls/single.html', {})
def contact(request):
    return render(request, 'polls/contact.html', {})


def detail(request, question_id):
    return render(request, 'polls/detail.html', {})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)