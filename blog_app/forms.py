<<<<<<< HEAD

from django import forms
from .models import Contact
from django import forms
from .models import Contact
from django.core.exceptions import ValidationError
class ContactUsForm(forms.ModelForm):
    INTRO_METHOD_CHOICES=[
        ('search','از طریق جست و جو در اینترنت'),
        ('friend','معرفی دوستان')
    ]

    BIRTH_YEAR_CHOICES=[
        ('','Enter your year of birth'),
        ('1399','1399'),
        ('1400','1400'),
        ('1401','1401'),
        ('1402','1402'),
        ('1403','1403'),
        ('1404','1404'),
    ]
    
    name = forms.CharField(
        label='Your Name',
        max_length=100,
        error_messages={'required': 'Please enter your name ❌'},
        widget=forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control', 'autofocus': 'autofocus'})
    )
    email = forms.EmailField(
        label='Your Email',
        error_messages={
            'required': 'Email is required ❌',
            'invalid': 'Please enter a valid email ⚠️',
        },
        widget=forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-control'})
    )
    subject = forms.CharField(
        label='Your Subject',
        max_length=200,
        error_messages={'required': 'Please write a subject ⚠️'},
        widget=forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'form-control'})
    )
    message = forms.CharField(
        label='Your Message',
        error_messages={'required': 'You cannot send an empty message!'},
        widget=forms.Textarea(attrs={'placeholder': 'Your Message', 'class': 'form-control'})
    )
    birth_year=forms.ChoiceField(
        label='year of birth',
        choices=BIRTH_YEAR_CHOICES,
        widget=forms.Select(attrs={'class':'form-control'}),
       
        # birth_year=forms.DateField(widget=forms.selectDateWidget(years=birth_year_choices,attrs={'form-contorol'}))
    )
    intro_method=forms.ChoiceField(
        label='How to get to know the site',
        choices=INTRO_METHOD_CHOICES, 
        widget=forms.RadioSelect(attrs={'style':'transform:acale(0.5);margin:0 10px 0 0 ;'})
    )


    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message','intro_method', 'birth_year']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        message = cleaned_data.get('message')

        if name and message and name == message:
            # اگر می‌خوای این خطا در بالای فرم نمایش داده بشه (نه برای فیلد خاص)
            raise ValidationError('⚠️ Your name and message cannot be the same!')
        return cleaned_data

    # ✅ بررسی فیلد خاص (و بازگرداندن خطاهای سفارشی)
    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if '@' in name:
            raise ValidationError('@ cannot be part of your name ⚠️')
        return name
# -----------------------------------------------------------------------------------------



    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     super().full_clean()
    #     for field_name, field in self.fields.items():
    #         # کلاس پایه
    #         classes = field.widget.attrs.get('class', '')
    #         field.widget.attrs['class'] = f'{classes} form-control'.strip()
    #         # اگر خطا داشت کلاس is-invalid اضافه می‌شود
    #         if self.errors.get(field_name):
    #             field.widget.attrs['class'] += ' is-invalid'


=======
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
    widget=forms.Select(attrs={'class': 'form-control','style':'font-weight:bold'}),
    label='سال تولد',
    
) 
   intro_method = forms.ChoiceField(
        choices=Message.INTRO_METHOD_CHOICES,
        widget=forms.RadioSelect(attrs={
            'style': 'transform: scale(0.5); margin: 0 10px 0 0;',
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
    
    
>>>>>>> f41c882f22339677ede193f7aa3f0088eacc4edc
