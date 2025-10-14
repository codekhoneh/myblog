from django import forms
from .models import ContactMessage
from django.core.validators import ValidationError

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'text']
 
    def clean(self):
        name=self.cleaned_data.get('name')
        text=self.cleaned_data.get('text')
       
        if name==text:
            raise ValidationError('خطا:نام و متن نظرات نمی تواند یکسان باشد',code='name_text_same')
    def clean_name(self):
        name=self.cleaned_data.get('name')
        if '@' or '*'  in name:
             raise ValidationError('@ یا* نمی تواند در نام استفاده شود',code='@_in code')
        return name
    
    
