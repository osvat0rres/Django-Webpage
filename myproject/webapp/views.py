from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from myproject.settings import *  
from django.core.mail import send_mail

def index(request):
    return render(request, 'index.html')


def singup(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('index')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('index')
        
        if User.objects.filter(email=email):
            messages.error(request,"Email already exits.")
            return redirect ('index')
        
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters.")
            
        
        if password  != confirm_password:
            messages.error(request, "Passwords do not match.")
            
        
        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric.")
            return redirect('index')
        
            
        
        # Create user
        myuser = User.objects.create_user(
            username,
            email,
            password
        )

        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.save()

        messages.success(request, "Your account has been successfully created.")
        
        subject = "Welcome to the website"
        
        message = "Hello" + myuser.first_name + "!! \n" + "Welcome to teh website. We are glad to have you\n" + "Please confer your email."
        from_email = EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        return redirect('index')
    
    

    return render(request, 'singup.html')


def singin(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'index.html' , {'fname': fname})
        else:
            messages.error(request,"Invalid unsername or password")
            return redirect('index')
            
    
    return render(request, 'singin.html')


def singout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('index')