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
        
        user = authenticate(username=username, password=password)
        if user is None:
          raise ValidationError("⚠️ اطلاعات وارد شده صحیح نیست. لطفاً دوباره تلاش کنید!", code="invalid_info")     
        return   
        
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
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username' , 'first_name' , 'last_name' , 'email')