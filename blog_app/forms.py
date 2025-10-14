from django import forms
from .models import ContactMessage
from django.core.validators import ValidationError

class ContactUsForm(forms.ModelForm):



   BIRTH_YEAR_CHOICES = [
    ('', 'سال تولد را انتخاب کنید'),  # گزینه‌ی پیش‌فرض (placeholder)
    ('1399', '1399'),
    ('1400', '1400'),
    ('1401', '1401'),
    ('1402', '1402'),
    ('1403', '1403'),
    ('1404', '1404'),
    ]

   birth_year = forms.ChoiceField(
    choices=BIRTH_YEAR_CHOICES,
    widget=forms.Select(attrs={'class': 'form-control'}),
    label='سال تولد'
)

   class Meta:
    model = ContactMessage
    fields = ['name', 'text', 'email']
    widgets = {
        'name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام خود را وارد کنید'
        }),
        'email': forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ایمیل خود را وارد کنید'
        }),
        'text': forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'متن پیام خود را بنویسید'
        }),
    }
 
   def clean(self):
        name=self.cleaned_data.get('name')
          
        text=self.cleaned_data.get('text')
        text=self.cleaned_data.get('email')

       
        if name==text:
            raise ValidationError('خطا:نام و متن نظرات نمی تواند یکسان باشد',code='name_text_same')
   def clean_name(self):
        name=self.cleaned_data.get('name')
        if '@'   in name:
             raise ValidationError('@ یا* نمی تواند در نام استفاده شود',code='@_in code')
        return name
    
    
