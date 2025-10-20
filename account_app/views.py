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
<<<<<<< HEAD
            login(request,user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('/')
            
    return render(request,'account_app/login.html',context={})
=======
            login(request, user)
            next_url = request.POST.get('next')
            return redirect(next_url if next_url else '/')
    return render(request, 'account_app/login.html', context={})

>>>>>>> f41c882f22339677ede193f7aa3f0088eacc4edc
def user_logout(request):
    logout(request)
    return redirect('/')

<<<<<<< HEAD

=======
>>>>>>> f41c882f22339677ede193f7aa3f0088eacc4edc
def user_register(request):
    context = {'errors': []}
    if request.user.is_authenticated:
        return redirect('/')
<<<<<<< HEAD
    
    # دریافت next از پارامتر GET
    next_url = request.GET.get('next', '')
    context['next'] = next_url
    
    if request.method == "POST":
=======
    elif request.method == 'POST':
>>>>>>> f41c882f22339677ede193f7aa3f0088eacc4edc
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        password2 = request.POST.get('password2', '').strip()
<<<<<<< HEAD
        
        # بررسی خطاها
        if password != password2:
            context['errors'].append('Passwords do not match')
        
        if User.objects.filter(username=username).exists():
            context['errors'].append('Username already exists')
        
        if User.objects.filter(email=email).exists():
            context['errors'].append('Email already exists')
        
        # اگر خطایی وجود دارد، فرم را دوباره نمایش بده
        if context['errors']:
            return render(request, 'account_app/register.html', context)
        
        # ایجاد کاربر جدید
        user1 = User.objects.create_user(username=username, password=password, email=email)
        login(request, user1)
        
        # دریافت next از POST (اگر وجود دارد) یا از GET
        next_url = request.POST.get('next') or request.GET.get('next')
        if next_url:
            return redirect(next_url)
        else:
            return redirect('/')
    
    return render(request, 'account_app/register.html', context)
# def user_register(request):
#     context = {'errors' : []}
#     if request.user.is_authenticated == True:
#        return redirect('/')
#     elif request.method == "POST":
#         username = request.POST.get('username','').strip()
#         email = request.POST.get('email','').strip()
#         password = request.POST.get('password','').strip()
#         password2 = request.POST.get('password2','').strip()
#         if password != password2 or  User.objects.filter(username=username).exists():
#             context['errors'].append('password are not send or user name reapeater')
#         if User.objects.filter(username=username).exists():
#             context['errors'].append('username reapeater')
#         if User.objects.filter(email=email).exists():

#             context['errors'].append('Email already exosts')
#             return render(request,'account_app/register.html',context)

                
#         user1 =User.objects.create_user(username=username,password=password,email=email)
#         login(request,user1)
#         next_url = request.GET.get('next')
#         if next_url:
#             return redirect(next_url)
#         else:
#             return redirect('/')
#         # return redirect('/')
#     return render(request,'account_app/register.html',context={})
# # Create your views here.
=======
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
>>>>>>> f41c882f22339677ede193f7aa3f0088eacc4edc
