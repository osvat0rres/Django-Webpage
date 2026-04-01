from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('singup/', views.singup, name='singup'),
    path('singin/', views.singin, name='singin'),
    path('singout/', views.singout, name='singout'),
]