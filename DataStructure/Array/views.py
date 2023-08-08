from  django.shortcut import render
from django.http import  httpresponse

def index(reqeust):
    return  render(reqeust,'index html')
def main(request):
    return render(request,'hello brother')
def login(request):
    return render(request,'registration html')

