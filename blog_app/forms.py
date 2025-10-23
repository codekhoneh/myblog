from django import forms
from .models import Message
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
    widget=forms.Select(attrs={'class': 'form-control','style':'font-weight:bolder;font-size:0.9rem'}),
    label='سال تولد',
    
) 
   intro_method = forms.ChoiceField(
        choices=Message.INTRO_METHOD_CHOICES,
        widget=forms.RadioSelect(attrs={
            'style': 'transform: scale(0.5); margin: 0 10px 0 0;font-weight:bolder;',
        }),
        label='نحوه آشنایی با سایت'
    )

   class Meta:
    model = Message
    fields = ['name', 'text', 'email','intro_method']
    widgets = {
        'name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام خود را وارد کنید',
            'style':'font-size:1.2rem;font;font-weight:bolder;'
        }),
        'email': forms.EmailInput(attrs={
            'placeholder': 'ایمیل خود را وارد کنید',
            'style':'font-size:1.2rem;font;font-weight:bolder;'
        }),
        'text': forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'متن پیام خود را بنویسید',
            'style':'font-size:1.2rem;font;font-weight:bolder;'
        }),
    }
 
   def clean(self):
        cleaned_data = super().clean()
        name=self.cleaned_data.get('name')
          
        text=self.cleaned_data.get('text')

       
        if name==text:
            self.add_error('name','خطا:نام و متن نظرات نمی تواند یکسان باشد')
        return cleaned_data
   def clean_name(self):
        name=self.cleaned_data.get('name')
        if '@'   in name:
             raise ValidationError('@ یا* نمی تواند در نام استفاده شود',code='@_in code')
        return name
    
    
