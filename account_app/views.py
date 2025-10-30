from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from .forms import LoginForm, RegisterForm 
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

def user_logout(request):
    logout(request)
    return redirect('/')

def user_register(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username, password=password, email=email)
            login(request, user)
            next_url = request.POST.get('next')
            return redirect(next_url if next_url else '/')
    else:
        form = RegisterForm()

    return render(request, 'account_app/register.html', {'form': form})
# Create your views here.


from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserEditForm, ProfileForm
from .models import profile as ProfileModel


@login_required
def user_edit(request):
    user = request.user
    profile_obj, created = ProfileModel.objects.get_or_create(myuser=user)

    if request.method == 'POST':
        user_form = UserEditForm(instance=user, data=request.POST)
        profile_form = ProfileForm(instance=profile_obj, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile = profile_form.save(commit=False)
            profile.myuser = user
            profile.save()
            messages.success(request, 'اطلاعات شما با موفقیت ثبت شد')
            return redirect('home:main')
        else:
            # let template show errors
            pass
    else:
        user_form = UserEditForm(instance=user)
        profile_form = ProfileForm(instance=profile_obj)

    return render(request, 'account_app/edit.html', {'myform': user_form, 'pform': profile_form, 'user': user})