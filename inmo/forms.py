from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Usuario')
    email = forms.EmailField(label='Correo')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']
        help_texts = {k:"" for k in fields } 

class EditProfileForm(UserChangeForm):

    username = forms.CharField(label='Usuario')
    email = forms.EmailField(label='Correo')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    password = None
    
    class Meta:
        model = User
        fields = ['username',
        'email',
        'first_name',
        'last_name']
from .models import ComunaPropiedad
class ComunaForm(forms.ModelForm):
    class Meta:
        model = ComunaPropiedad
        fields = ['nombreComuna']

    def clean_nombreComuna(self):
        nombre_comuna = self.cleaned_data['nombreComuna']
        # Realiza cualquier validación adicional que puedas necesitar
        return nombre_comuna
