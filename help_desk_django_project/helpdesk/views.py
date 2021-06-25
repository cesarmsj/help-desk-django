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
def cliente_home(request):
    return render(request, 'cliente/cliente_home.html')

@login_required(login_url='cliente_login')
def cliente_list(request, template_name='cliente/cliente_list.html'):
    cliente = Cliente.objects.all()
    clientes = {'cliente': cliente}
    return render(request, template_name, clientes)


def cliente_create(request):
    if request.user.is_authenticated:
        return redirect('cliente_home')
    else:
        form = CreateUserForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                user = form.save()
                user.refresh_from_db()
                user.save()
                username = form.cleaned_data.get('username')
                messages.success(request, 'Conta criada para o cliente ' + username)
                return redirect('cliente_login')
            else:
                messages.error(request, 'Erro ao tentar cadastrar o usuário')
                return redirect('cliente_create')

    context = {'form': form}
    return render(request, 'cliente/cliente_form.html', context)

@login_required(login_url='atendente_login')
def cliente_delete(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    if request.method == "POST":
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'cliente/cliente_delete.html', {'cliente': cliente})

@login_required(login_url='atendente_login')
def atendente_home(request):
    return render(request, 'atendente/atendente_home.html')

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
                #user_logged = User.objects.get(user_id=request.user.id)
                #chamado = Chamado.objects.filter(fk_cliente=cli.id)
                if Atendente.objects.filter(user_id=request.user.id).exists():
                    return redirect('atendente_home')
                elif Cliente.objects.filter(user_id=request.user.id).exists():
                    return redirect('cliente_home')
                else:
                    messages.error(request, 'Houve uma falha ao tentar verificar o perfil do usuário')
                    return redirect('home')
            else:
                messages.error(request, 'Usuário ou senha incorreto')
        context = {}
        return render(request, 'atendente/atendente_login.html', context)

#@login_required(login_url='atendente_login')
#def atendente_list(request, template_name='atendente/atendente_list.html'):
#    atendente = Atendente.objects.all()
#    atendentes = {'cliente': atendente}
#    return render(request, template_name, atendentes)

def atendente_create(request):
    if request.user.is_authenticated:
        return redirect('atendente_home')
    else:
        form = CreateUserForm(request.POST)
        #atendente_form = AtendenteForm(request.POST or None)

        if request.method == 'POST':
            if form.is_valid(): #and atendente_form.is_valid():
                user = form.save()
                #atendente = atendente_form.save(commit=False)
                #atendente.user = user
                #atendente.save()
                username = form.cleaned_data.get('username')
                messages.success(request, 'Conta criada para o atendente ' + username)
                return redirect('atendente_login')
            else:
                #messages.error(request, 'Erro ao tentar cadastrar o usuário')
                return redirect('atendente_create')

    context = {'form': form}
    return render(request, 'atendente/atendente_form.html', context)

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
#def atendente_delete(request, pk):
#    atendente = Atendente.objects.get(pk=pk)
#    if request.method == "POST":
#        atendente.delete()
#        return redirect('atendente_list')
#    return render(request, 'atendente_delete', {'atendente': atendente})

@login_required(login_url='cliente_login')
def chamado_create(request, pk):
    form = ChamadoForm(request.POST)
    cliente = Cliente.objects.get(user_id=pk)
    form.instance.fk_cliente = cliente

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Chamado aberto!')
            return redirect('chamado_list')
        else:
            messages.error(request, 'Houve um problema ao tentar abrir o chamado.')
            return redirect('chamado_list')
    context = {'form': form}
    return render(request, 'chamado/chamado_form.html', context)

@login_required(login_url='cliente_login')
def chamado_list(request):
    cli = Cliente.objects.get(user_id=request.user.id)
    chamado = Chamado.objects.filter(fk_cliente=cli.id)
    context = {'chamado': chamado}
    return render(request, 'chamado/chamado_list.html', context)

def chamado_interacao_create(request, id_chamado):
    form = ChamadoInteracaoForm(request.POST)
    chamado = Chamado.objects.get(id=id_chamado)
    form.instance.fk_chamado = chamado

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Interação adicionada!')
            return redirect('chamado_interacao_list', id_chamado)
        else:
            messages.error(request, 'Houve um problema ao tentar adicionar a interação ao chamado.')
            return redirect('chamado_interacao_list', id_chamado)
    context = {'form': form, 'chamado': id_chamado}
    return render(request, 'chamado_interacao/chamado_interacao_form.html', context)

def chamado_interacao_list(request, chamado):
    chamado_interacao = Chamado_Interacao.objects.filter(fk_chamado=chamado)
    context = {'interacao': chamado_interacao, 'chamado': chamado }
    return render(request, 'chamado_interacao/chamado_interacao_list.html', context)

