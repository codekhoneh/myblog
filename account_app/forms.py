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
            raise ValidationError('اطلاعات وارد شده صحیح نیست', code='invalid_info')
        return cleaned_data
