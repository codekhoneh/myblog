from django import forms 
from django.contrib.auth import authenticate 
from django.forms import ValidationError


 
from django import forms 
class LoginForm(forms.Form): 
    username=forms.CharField(max_length=50,widget=forms.TextInput(attrs={"class":"input100"})) 
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"input100"}))
    

    
    def clean(self): 
        cleaned_data = super().clean() 
        username = cleaned_data.get('username') 
        password = cleaned_data.get('password') 
 
        user = authenticate(username=username, password=password) 
        if user is None: 
            raise ValidationError('اطلاعات وارد شده صحیح نیست ', code='invalid_info') 
        return cleaned_data 
    
class RegisterForm(forms.Form): 
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "input100"})) 
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "input100"})) 
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "input100"})) 
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput(attrs={"class": "input100"})) 
 
    def clean_username(self): 
        username = self.cleaned_data.get('username') 
        if User.objects.filter(username=username).exists(): 
            raise ValidationError('This username is already taken.') 
        return username 
 
    def clean_email(self): 
        email = self.cleaned_data.get('email') 
        if User.objects.filter(email=email).exists(): 
            raise ValidationError('This email is already registered.') 
        return email 
 
    def clean(self): 
        cleaned_data = super().clean() 
        password = cleaned_data.get('password') 
        password2 = cleaned_data.get('password2') 
        if password and password2 and password != password2: 
            raise ValidationError('Passwords do not match.') 
        return cleaned_data 
    
from django.contrib.auth.models import User 
class UserEditForm(forms.ModelForm): 
    class Meta: 
        model = User 
        fields = ('username', 'first_name', 'last_name', 'email')

from .models import profile as ProfileModel

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ('family', 'nationalcode', 'image')
        widgets = {
            'family': forms.TextInput(attrs={'class': 'form-control'}),
            'nationalcode': forms.TextInput(attrs={'class': 'form-control'}),
        }