from django.forms import ModelForm
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Chamado, Chamado_Interacao

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={'type': 'email', 'required': 'required'}),
        }

class ChamadoForm(ModelForm):
    class Meta:
        model = Chamado
        fields = '__all__'
        widgets = {
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'type': 'date', 'required': 'required'}),
        }

class CreateChamadoInteracaoForm(ModelForm):
    class Meta:
        model = Chamado_Interacao
        fields = ['descricao']
        widgets = {
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'type': 'date', 'required': 'required'}),
        }
