from django.forms import ModelForm
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Atendente, Chamado, Chamado_Interacao, Cliente

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={'type': 'email', 'required': 'required'}),
        }

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        exclude = ['user']

class AtendenteForm(ModelForm):
    class Meta:
        model = Atendente
        exclude = ['user']

class ChamadoForm(ModelForm):
    class Meta:
        model = Chamado
        fields = ['descricao']
        widgets = {
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'type': 'text', 'required': 'required', 'placeholder':'Em que podemos lhe ajudar? Escreva aqui.'}),
        }

class ChamadoInteracaoForm(ModelForm):
    class Meta:
        model = Chamado_Interacao
        fields = ['interacao']
        widgets = {
            'interacao': forms.Textarea(attrs={'class': 'form-control', 'type': 'text', 'required': 'required', 'placeholder':'Em que podemos lhe ajudar? Escreva aqui.', 'rows': 2, 'maxlength':100}),
        }
