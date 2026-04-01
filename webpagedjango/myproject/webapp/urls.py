from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('admin/', admin.site.urls),
    path('singup/', views.singup, name='singup'),
    path('singin/', views.singin, name='singin'),
    path('singout/', views.singout, name='singout'),
]