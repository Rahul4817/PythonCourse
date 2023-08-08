from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')
def main(request):
    return HttpResponse('Hello Brother')

def about(request):
    return HttpResponse('This is about me')

def login(request):
    return render(request,'registration.html')