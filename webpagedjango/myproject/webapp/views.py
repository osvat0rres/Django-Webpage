
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Post


# Home / Feed
@login_required
def index(request):


    if request.method == 'POST':
        content = request.POST.get('content')

        if content:
            Post.objects.create(
                user=request.user,
                content=content
            )
            return redirect('index')

   
    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'index.html', {
        'posts': posts
    })


# Signup
def singup(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        # Password match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('index')

        # Username exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('index')

        # Email exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('index')

        # Username length
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters.")
            return redirect('index')

        # Username validation
        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric.")
            return redirect('index')

        # Create user
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


# Signin
def singin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)

            return redirect('index')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('index')

    return render(request, 'singin.html')



def singout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('index')



@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.user == request.user:
        post.delete()

    return redirect('index')

