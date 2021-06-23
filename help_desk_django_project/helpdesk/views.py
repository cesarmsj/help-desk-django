from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms

# Create your views here.

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


def home(request, template_name='home/home.html'):
    return render(request, template_name)

def cliente_login(request):
    if request.user.is_authenticated:
        return redirect('cliente_home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('cliente_home')
            else:
                messages.info(request, 'Usuário ou senha incorreto')
        context = {}
        return render(request, 'cliente/cliente_login.html', context)

def logout(request):
        logout(request)
        return redirect('home')

def cliente_home(request, template_name='cliente/cliente_home.html'):
    chamado = Chamado.objects.all()
    chamados = {'chamado': chamado}
    return render(request, template_name, chamados)

def cliente_list(request, template_name='cliente/cliente_list.html'):
    cliente = Cliente.objects.all()
    clientes = {'cliente': cliente}
    return render(request, template_name, clientes)

def cliente_create(request, template_name='cliente/cliente_form.html'):
    if request.user.is_authenticated:
        return redirect('cliente_home')
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.sucess(request, 'Conta criada para o usuário ' + user)

            return redirect('cliente_login')

    context = {'form': form}
    return render(request, template_name, context)

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

def atendente_login(request):
    if request.user.is_authenticated:
        return redirect('atendente_home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('atendente_home')
            else:
                messages.info(request, 'Usuário ou senha incorreto')
        context = {}
        return render(request, 'cliente/cliente_login.html', context)

def atendente_list(request, template_name='atendente/atendente_list.html'):
    atendente = Atendente.objects.all()
    atendentes = {'cliente': atendente}
    return render(request, template_name, atendentes)

def atendente_create(request, template_name='atendente/atendente_form.html'):
    if request.user.is_authenticated:
        return redirect('atendente_home')
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.sucess(request, 'Conta criada para o usuário ' + user)

            return redirect('atendente_login')

    context = {'form': form}
    return render(request, template_name, context)

#def atendente_update(request, pk, template_name='atendente/atendente_form.html'):
#    atendente = get_object_or_404(Atendente, pk=pk)
#    if request.method == "POST":
#        form = AtendenteForm(request.POST, instance=atendente)
#        if form.is_valid():
#            cliente = form.save()
#            return redirect('atendente_list')
#    else:
#        form = AtendenteForm(instance=atendente)
#    return render(request, template_name, {'form': form})

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

