from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def user_login(request):
    if request.user.is_authenticated:
        next_url = request.POST.get('next')
        return redirect(next_url if next_url else '/')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next')
            return redirect(next_url if next_url else '/')
    return render(request, 'account_app/login.html', context={})

def user_logout(request):
    logout(request)
    return redirect('/')

def user_register(request):
    context = {'errors': []}
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        password2 = request.POST.get('password2', '').strip()
        if password != password2 or User.objects.filter(username=username).exists():
            context['errors'].append('Passwords do not match or username already exists.')
        if User.objects.filter(email=email).exists():
            context['errors'].append('Email already exists.')
        if not context['errors']:
            user = User.objects.create_user(username=username, password=password, email=email)
            login(request, user)
            next_url = request.POST.get('next')
            return redirect(next_url if next_url else '/')
 
    return render(request, 'account_app/register.html', context={})
# Create your views here.
