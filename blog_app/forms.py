from django import forms 
from django.core.exceptions import ValidationError
from .models import Message

class ContactUsForm(forms.ModelForm): 
    text=forms.CharField(
        max_length=50,
        label='your message',
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'متن پیام را وارد کنید','class': 'form-control','style':'font-weight:bolder ;font-size:1.3rem'})
    )
    name=forms.CharField(
        max_length=5,
        label='your name',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'نام خود را وارد کنید','class': 'form-control','style':'font-weight:bolder ;font-size:1.3rem'})
    )
    birth_year_choices=[
            ('','سال تولد خود را انتخاب کنید'),
            ('1399','1399'),
            ('1400','1400'),
            ('1401','1401'),
            ('1402','1402'),
            ('1403','1403'),
            ('1404','1404')
        ]
    birth_year=forms.ChoiceField(choices=birth_year_choices,required=False,widget=forms.Select(attrs={'class':'form-control','style':'font-weight:bolder ;'}),)
        
    tahsilat_choice=[('sikl','sikl'),('deplom','Diplom'),('karshenas','karshenas'),('arshad','arshad'),('dr','dr')] 
    tahsilat=forms.ChoiceField(widget=forms.RadioSelect(),choices=tahsilat_choice)
    favorits_program_language_choice=[('Python','python'),('django','Django'),('html','Html'),('css','Css')] 
    language_favorits=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(),choices=favorits_program_language_choice)
    intro_method=forms.ChoiceField(choices=Message.INTRO_METHOD_CHOICES,required=False,
                                       widget=forms.RadioSelect(attrs={'style':'transform:scale(0.5);margin:0 10 0 0'}),
                                       label='نحوه آشنایی با سایت')
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        text = cleaned_data.get('text')
        if name == text:
            self.add_error('name', 'نام و پیام نباید یکسان باشند')
        return cleaned_data

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name and '@' in name:
            raise ValidationError('@ نمی‌تواند در نام باشد', code='@_in_name')
        return name
    class Meta:
        model = Message
        fields = ['title','text','email']
        widgets = {
            'name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'نام خود را وارد کنید'
            }),
            'email':forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder':'ایمیل خود را وارد کنید',
                'style':'font-weight:bolder ;font-size:1.3rem'
            }),
            'text':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'متن خود را وارد کنید'

            })
        }
