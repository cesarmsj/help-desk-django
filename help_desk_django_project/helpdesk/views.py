from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import *
from django import forms

# Create your views here.
def home(request, template_name='home/home.html'):
    return render(request, template_name)

class ClienteLoginForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['username', 'password' ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control col-4', 'type': 'text', 'required': 'required'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control col-4', 'type': 'password', 'required': 'required'}),
        }

class AtendenteLoginForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['username', 'password' ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control col-4', 'type': 'text', 'required': 'required'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control col-4', 'type': 'password', 'required': 'required'})
        }

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['username','password', 'nome', 'nascimento', 'email', 'sexo', 'cidade']
        widgets = {
            'password': forms.PasswordInput(),
            'confirmPassword': forms.PasswordInput(),
            'nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': 'required'}),
        }

class AtendenteForm(ModelForm):
    class Meta:
        model = Atendente
        fields = ['username','password', 'nome', 'nascimento', 'email', 'sexo', 'cidade']
        widgets = {
            'password': forms.PasswordInput(),
            'confirmPassword': forms.PasswordInput(),
            'StartDate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': 'required'}),
        }

class ChamadoForm(ModelForm):
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

def cliente_login(request, template_name='cliente/cliente_login.html'):
    form = ClienteLoginForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cliente_home')
    return render(request, template_name, {'form': form})

def cliente_logout(request, template_name='cliente/cliente_logout.html'):
        return redirect(template_name)

def cliente_home(request, template_name='cliente/cliente_home.html'):
    chamado = Chamado.objects.all()
    chamados = {'chamado': chamado}
    return render(request, template_name, chamados)

def cliente_list(request, template_name='cliente/cliente_list.html'):
    cliente = Cliente.objects.all()
    clientes = {'cliente': cliente}
    return render(request, template_name, clientes)

def cliente_create(request, template_name='cliente/cliente_form.html'):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cliente_list')
    return render(request, template_name, {'form': form})

def cliente_update(request, pk, template_name='cliente/cliente_form.html'):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save()
            return redirect('cliente_list')
    else:
            form = ClienteForm(instance=cliente)
    return render(request, template_name, {'form': form})

def cliente_delete(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    if request.method == "POST":
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'cliente/cliente_delete.html', {'cliente': cliente})

def atendente_home(request, template_name='atendente/atendente_home.html'):
    chamado = Chamado.objects.all()
    chamados = {'chamado': chamado}
    return render(request, template_name, chamados)

def atendente_login(request, template_name='atendente/atendente_login.html'):
    form = AtendenteLoginForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('atendente_home')
    return render(request, template_name, {'form': form})

def atendente_list(request, template_name='atendente/atendente_list.html'):
    atendente = Atendente.objects.all()
    atendentes = {'cliente': atendente}
    return render(request, template_name, atendentes)

def atendente_create(request, template_name='atendente/atendente_form.html'):
    form = AtendenteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('atendente_list')
    return render(request, template_name, {'form': form})

def atendente_update(request, pk, template_name='atendente/atendente_form.html'):
    atendente = get_object_or_404(Atendente, pk=pk)
    if request.method == "POST":
        form = AtendenteForm(request.POST, instance=atendente)
        if form.is_valid():
            cliente = form.save()
            return redirect('atendente_list')
    else:
        form = AtendenteForm(instance=atendente)
    return render(request, template_name, {'form': form})

def atendente_delete(request, pk):
    atendente = Atendente.objects.get(pk=pk)
    if request.method == "POST":
        atendente.delete()
        return redirect('atendente_list')
    return render(request, 'atendente_delete', {'atendente': atendente})

def chamado_create(request, template_name='chamado/chamado_form.html'):
    form = ChamadoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('chamado_list')
    return render(request, template_name, {'form': form})

