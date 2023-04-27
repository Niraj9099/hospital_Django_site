from django import forms
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class myform(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Conform Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'Address', 'city', 'state', 'pincode','catagory','user_profile']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'pincode': forms.NumberInput(attrs={'class': 'form-control'}),
            'catagory': forms.Select(attrs={'class': 'form-control'}),
            'user_profile': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class loginForm(AuthenticationForm):
    class Meta:
        model = UserProfile
        fields = ['email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }