from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
import re

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=10)
    role = forms.ChoiceField(choices=[('Member', 'Member'), ('Volunteer', 'Volunteer')])

    class Meta:
        model = User
        fields = ['email', 'phone_number', 'role', 'password1', 'password2']

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if not re.match(r'^\d{10}$', phone):
            raise forms.ValidationError("Phone number must be 10 digits.")
        return phone

    def clean_password2(self):
        p = self.cleaned_data.get('password2')
        if not p:
            return p
        if len(p) < 8:
            raise forms.ValidationError("Password must be at least 8 characters.")
        if not re.search(r'[A-Z]', p):
            raise forms.ValidationError("Password must contain at least one uppercase letter.")
        if not re.search(r'[a-z]', p):
            raise forms.ValidationError("Password must contain at least one lowercase letter.")
        if not re.search(r'[0-9]', p):
            raise forms.ValidationError("Password must contain at least one number.")
        return p