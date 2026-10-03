from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil, Inmueble


class RegistroUsuarioForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, required=True, label="Nombre")
    last_name = forms.CharField(max_length=150, required=True, label="Apellido")
    email = forms.EmailField(required=True, label="Correo electrónico")
    tipo_usuario = forms.ChoiceField(choices=Perfil.TIPO_USUARIO_CHOICES, label="Tipo de Usuario")
    rut = forms.CharField(max_length=15, required=False, label="RUT")
    telefono = forms.CharField(max_length=20, required=False, label="Teléfono")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=150, required=True, label="Nombre")
    last_name = forms.CharField(max_length=150, required=True, label="Apellido")
    email = forms.EmailField(required=True, label="Correo electrónico")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class PerfilUpdateForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['tipo_usuario', 'rut', 'telefono']
        labels = {
            'tipo_usuario': 'Tipo de Usuario',
            'rut': 'RUT',
            'telefono': 'Teléfono',
        }
class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = ['descripcion', 'direccion', 'tipo_inmueble', 'valor_arriendo', 'disponible', 'comuna']
        labels = {
            'descripcion': 'Descripción',
            'direccion': 'Dirección',
            'tipo_inmueble': 'Tipo de Inmueble',
            'valor_arriendo': 'Valor de Arriendo',
            'disponible': 'Disponible',
            'comuna': 'Comuna',
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'Ej: Casa luminosa de 3 dormitorios...'
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ej: Av. Siempre Viva 742'
            }),
            'tipo_inmueble': forms.Select(attrs={'class': 'form-select'}),
            'valor_arriendo': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ej: 450000'
            }),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input ms-2'}),
            'comuna': forms.Select(attrs={'class': 'form-select'}),
        }

class ActualizarInmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = ['descripcion', 'direccion', 'tipo_inmueble', 'valor_arriendo', 'disponible', 'comuna']
        labels = {
            'descripcion': 'Descripción',
            'direccion': 'Dirección',
            'tipo_inmueble': 'Tipo de Inmueble',
            'valor_arriendo': 'Valor de Arriendo',
            'disponible': 'Disponible',
            'comuna': 'Comuna',
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'Ej: Casa luminosa de 3 dormitorios...'
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ej: Av. Siempre Viva 742'
            }),
            'tipo_inmueble': forms.Select(attrs={'class': 'form-select'}),
            'valor_arriendo': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ej: 450000'
            }),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input ms-2'}),
            'comuna': forms.Select(attrs={'class': 'form-select'}),
        }