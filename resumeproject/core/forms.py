from django import forms
from .models import contactmodel

class ContactForm(forms.ModelForm):
    class Meta:
        model = contactmodel
        fields = ['name', 'email', 'phone', 'message']
