from django.urls import path
from myApp import views

urlpatterns =[
    path('',views.main,name='main'),
    path('index.html/',views.index,name='index.html'),
    path('registration.html/',views.login,name='registration.html'),
]
