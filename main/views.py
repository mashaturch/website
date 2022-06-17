from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def project(request):
    return render(request, 'main/project.html')


def price(request):
    return render(request, 'main/price.html')