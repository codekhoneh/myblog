from django import forms
from django.core.exceptions import ValidationError


class ContactUsForm(forms.Form):
    text = forms.CharField(
        max_length=1000,
        label='your message',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
    )
    name = forms.CharField(
        max_length=100,
        label='your name',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    birth_year_choices = [
        ('1399', '1399'), ('1400', '1400'), ('1401', '1401'),
        ('1402', '1402'), ('1403', '1403'), ('1404', '1404')
    ]
    birth_year = forms.ChoiceField(
        choices=birth_year_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def clean(self):
        cleaned = super().clean()
        name = cleaned.get('name')
        text = cleaned.get('text')
        if name and text and name == text:
            raise ValidationError('ERRORS: name and text are the same', code='name_text_same')
        return cleaned

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name and '@' in name:
            raise ValidationError('@ can not be used in name', code='at_in_name')
        return name