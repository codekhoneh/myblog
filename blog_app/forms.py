from django import forms
from .models import ContactMessage

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'text']
