from django import forms 
from django.core.exceptions import ValidationError
class ContactUsForm(forms.Form): 
    text=forms.CharField(
        max_length=5,
        label='your message',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'متن پیام را وارد کنید','class': 'form-control'})
    )
    name=forms.CharField(
        max_length=5,
        label='your name',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'نام خود را وارد کنید','class': 'form-control'})
    )
    def clean(self): 
        name=self.cleaned_data.get('name') 
        text=self.cleaned_data.get('text')
        birth_year_choices=['1399','1400','1401','1402','1403','1404']
        birth_year=forms.DateField(widget=forms.SelectDateWidget(years=birth_year_choices,attrs={'class':'form-control'}))
        tahsilat_choice=[('sikl','sikl'),('deplom','Diplom'),('karshenas','karshenas'),('arshad','arshad'),('dr','dr')] 
        tahsilat=forms.ChoiceField(widget=forms.RadioSelect(),choices=tahsilat_choice)
        favorits_program_language_choice=[('Python','python'),('django','Django'),('html','Html'),('css','Css')] 
        language_favorits=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(),choices=favorits_program_language_choice)  
        if name==text: 
            raise ValidationError('ERRORS:name and text same',code='name_text_same') 
    def clean_name(self): 
        name=self.cleaned_data.get('name') 
        if '@' in name: 
             raise ValidationError('@ can not be name',code='@_in code') 
        return name 