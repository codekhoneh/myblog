from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .forms import LoginForm
from .forms import RegisterForm , UserEditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def user_login(request):
    next_url = request.POST.get('next')
    if request.user.is_authenticated == True:
        
        return redirect(next_url if next_url else '/')
    if request.method == 'POST':
        myform = LoginForm(request.POST)
        if myform.is_valid():
            user = User.objects.get(username = myform.cleaned_data.get('username'))
            login(request,user)
            return redirect(next_url if next_url else '/')
    else:
        myform = LoginForm()
    return render(request, 'account_app/login.html', {'myform':myform})

def user_logout(request):
    logout(request)
    return redirect('/')

def user_register(request):
    next_url = request.POST.get('next')
    if request.user.is_authenticated:
        return redirect(next_url if next_url else '/')

    if request.method == 'POST':
        myforms = RegisterForm(request.POST)
        if myforms.is_valid():
            user2 = User.objects.create_user(
                username=myforms.cleaned_data.get('username'),
                password=myforms.cleaned_data.get('password'),  # ⚡ اصلاح شد
                email=myforms.cleaned_data.get('email')
            )
            login(request, user2)
            return redirect(next_url if next_url else '/')
        # اگر فرم معتبر نبود، همان فرم با ارورها به template برمی‌گردد
    else:
        myforms = RegisterForm()  # ⚡ فرم خالی برای GET

    return render(request, 'account_app/register.html', {'myforms': myforms})
def user_edit(request):
    user=request.user
    if request.method == 'POST':
        form3 = UserEditForm(request.POST , instance=user)
        if form3.is_valid():
            form3.save()
            messages.success(request, 'اطلاعات شما با موفقیت ذخیره شد ✅🚀😎')
            return redirect('home:main')
  
    else:
        form3 = UserEditForm(instance=user)
    return render(request , 'account_app/edit.html',{'myform3':form3})

            

# Create your views here.
