from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
# -----------------------لاگین با تابع-------------------------
# def user_login(request):
#     if request.user.is_authenticated==True:
#         return redirect('/')
#     elif request.method=='POST':
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         user=authenticate(request,username=username,password=password)
#         if user is not None:
#             login(request,user)
#             return redirect('/')
#     return render(request,'account_app/login.html',context={})
# ----------------------------لاگین با فرم---------------------------
from .forms import LoginForm
def user_login(request):
    if request.user.is_authenticated==True:
        return redirect('/')
    if request.method=='POST':
        myform=LoginForm(request.POST)
        if myform.is_valid():
            user=User.objects.get(username=myform.cleaned_data.get('username'))
            login(request,user)
            return redirect("/")       
    else:
        myform=LoginForm()   
    return render (request,'account_app/login.html',{"form":myform})

# -------------------------------وformمثل هم استlogot با تابع-----------------------------
def user_logout(request):
    logout(request)
    return redirect('/')
# ----------------------------------------

def user_register(request):
    context = {'errors' : []}
    if request.user.is_authenticated == True:
        return redirect('/')
    elif request.method == "POST":
        username = request.POST.get('username','').strip()
        email = request.POST.get('email','').strip()
        password = request.POST.get('password','').strip()
        password2 = request.POST.get('password2','').strip()
        if password != password2 or  User.objects.filter(username=username).exists():
            context['errors'].append('password are not send or user name reapeater')
        if User.objects.filter(username=username).exists():
            context['errors'].append('username reapeater')
        if User.objects.filter(email=email).exists():

            context['errors'].append('Email already exosts')
            return render(request,'account_app/register.html',context)

                
        user1 =User.objects.create_user(username=username,password=password,email=email)
        login(request,user1)
        return redirect('/')
    return render(request,'account_app/register.html',context={})
# Create your views here.
