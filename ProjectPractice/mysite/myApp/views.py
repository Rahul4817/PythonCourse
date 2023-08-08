from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def main(request):
    return HttpResponse('Hello im from myApp')

def index(request):
    return render(request, 'myApp/index.html')

def login(request):
    return render(request, 'myApp/registration.html')
