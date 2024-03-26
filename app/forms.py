# app/forms.py

from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','password', 'name', 'phone', 'dob', 'city', 'user_type']  # Fields you want to include in the form
