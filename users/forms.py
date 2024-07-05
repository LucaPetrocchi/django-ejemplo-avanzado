from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='email requerido')
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
        ]
        
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'email': forms.EmailInput(
                attrs={'class': 'form-control'}
            ),
            'password1': forms.PasswordInput(
                attrs={'class': 'form-control'}
            ),
            'password2': forms.PasswordInput(
                attrs={'class': 'form-control'}
            ),
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'required' : 'required'}
            ),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control'}
            )
            
        }
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_exists = User.objects.filter(email=email).exists()
        if email_exists:
            raise ValidationError('El email ya esta registrado')
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_staff = False
        user.is_superuser = False
        if commit:
            user.save()
        return user