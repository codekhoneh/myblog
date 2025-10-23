from django import forms
from django.contrib.auth import authenticate
from django.forms import ValidationError
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'input100'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input100'}))
 

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username','').strip()
        password = cleaned_data.get('password')
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError('نام کاربری یا رمز عبور اشتباه است.')

        # 2️⃣ بررسی پسورد برای همان یوزرنیم
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('رمز عبور اشتباه است.')
class RegisterForm(forms.Form):
      
      username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'input100'}))
      password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input100'}))
      password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input100'}))
      email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input100'}))
      def clean(self):
            cleaned_data =  super().clean()
            username = cleaned_data.get('username','').strip()
            password = cleaned_data.get('password','').strip()
            password2 = cleaned_data.get('password2','').strip()
            if password != password2 or User.objects.filter(username=username).exists():
                raise ValidationError('Passwords do not match or username already exists.' , code = 'invalid_info')
            
      def clean_email(self):
            email = self.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                raise ValidationError ('Email already exists.' , code='invalid_email')
            return email
