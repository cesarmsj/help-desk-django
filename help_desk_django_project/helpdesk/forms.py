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

class CreateChamadoForm(ModelForm):
    class Meta:
        model = Chamado
        fields = ['status','data_abertura', 'data_fechamento', 'fk_atendente', 'descricao', 'fk_cliente']
        widgets = {
            'data_abertura': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': 'required'}),
            'data_fechamento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': 'required'})
        }

class ChamadoInteracaoForm(ModelForm):
    class Meta:
        model = Chamado_Interacao
        fields = ['fk_chamado','descricao']
        widgets = {
            'data_abertura': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': 'required'}),
            'data_fechamento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': 'required'})
        }
