from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from myproject.settings import *  
from django.core.mail import send_mail
from .models import Post
from django.contrib.auth.decorators import login_required

@login_required
def index(request):

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Post.objects.create(user=request.user, content=content)
            return redirect('index')

    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'index.html', {
        'fname': request.user.first_name,
        'posts': posts
    })



def singup(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

    
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('index')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('index')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('index')

        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters.")
            return redirect('index')

        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric.")
            return redirect('index')

    
        myuser = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.save()

        messages.success(request, "Your account has been successfully created.")


        return redirect('index')

    return render(request, 'singup.html')


def singin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')   
        else:
            messages.error(request, "Invalid username or password")
            return redirect('index')

    return render(request, 'singin.html')


def singout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('index')