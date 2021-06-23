import datetime

from django.shortcuts import render, redirect
from django.forms import inlineformset_factory

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

# Create your views here.

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
                messages.error(request, 'Usuário ou senha incorreto')
        context = {}
        return render(request, 'cliente/cliente_login.html', context)

def user_logout(request):
        logout(request)
        return redirect('home')

@login_required(login_url='cliente_login')
def cliente_home(request, template_name='cliente/cliente_home.html'):
    chamado = Chamado.objects.all()
    chamados = {'chamado': chamado}
    return render(request, template_name, chamados)

@login_required(login_url='cliente_login')
def cliente_list(request, template_name='cliente/cliente_list.html'):
    cliente = Cliente.objects.all()
    clientes = {'cliente': cliente}
    return render(request, template_name, clientes)


def cliente_create(request, template_name='cliente/cliente_form.html'):
    if request.user.is_authenticated:
        return redirect('cliente_home')
    else:
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Conta criada para o usuário ' + username)

            return redirect('cliente_login')

    context = {'form': form}
    return render(request, template_name, context)

@login_required(login_url='atendente_login')
def cliente_delete(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    if request.method == "POST":
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'cliente/cliente_delete.html', {'cliente': cliente})

@login_required(login_url='atendente_login')
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
                messages.error(request, 'Usuário ou senha incorreto')
        context = {}
        return render(request, 'cliente/cliente_login.html', context)

@login_required(login_url='atendente_login')
def atendente_list(request, template_name='atendente/atendente_list.html'):
    atendente = Atendente.objects.all()
    atendentes = {'cliente': atendente}
    return render(request, template_name, atendentes)

def atendente_create(request, template_name='atendente/atendente_form.html'):
    if request.user.is_authenticated:
        return redirect('atendente_home')
    else:
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Conta criada para o usuário ' + user)

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

@login_required(login_url='atendente_login')
def atendente_delete(request, pk):
    atendente = Atendente.objects.get(pk=pk)
    if request.method == "POST":
        atendente.delete()
        return redirect('atendente_list')
    return render(request, 'atendente_delete', {'atendente': atendente})

@login_required(login_url='cliente_login')
def chamado_create(request, pk):
    ChamadoFormSet = inlineformset_factory(Cliente, Chamado, fields=('data_abertura', 'data_fechamento'))
    cliente_logged = Cliente.objects.get(id=pk)
    cliente = cliente_logged.id
    if request.method == 'POST':
        form = ChamadoForm(request.POST or None)
        formset = ChamadoFormSet(request.POST, instance=cliente)
        if formset.is_valid():
            form.save()
            return redirect('chamado_list')
    context = {'form':formset}
    return render(request, 'chamado/chamado_create.html', context)

def chamado_interacao_create(request, chamado, template_name='chamado/chamadoInteracao_form.html'):
    chamado = Chamado.objects.get(pk=chamado)
    form = CreateChamadoInteracaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('chamado_interacao_list', pk=chamado.id)
    return render(request, template_name, {'form': form})

def chamado_interacao_list(request, chamado, template_name='atendente/atendente_list.html'):
    chamado_interacao = Atendente.objects.filter(chamado=chamado)
    chamado_interacoes = {'chamado_interacao': chamado_interacao}
    return render(request, template_name, chamado_interacoes)

