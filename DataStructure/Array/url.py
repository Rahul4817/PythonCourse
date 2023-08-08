from django.contrib import admin
from django.urls import path
from mysite import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index.html/',views.index, name='index.html'),
    path('registration.html/',views,name='registration.html')
    path('main/',views,name='hello brother')

]