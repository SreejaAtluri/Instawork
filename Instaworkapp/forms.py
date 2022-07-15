# from django.contrib.admin import forms
from django import forms
from django.forms import ModelForm, widgets
from Instaworkapp.models import Adddata

class AddForm(forms.ModelForm):
    class Meta:
        model = Adddata
        fields = '__all__'
        widgets={
            'firstname': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'First name'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phoneNumber': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
            'role': forms.RadioSelect(attrs={'class': ''}),
        }


