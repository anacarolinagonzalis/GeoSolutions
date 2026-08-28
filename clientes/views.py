
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Projeto
from .forms import ClienteForm, ProjetoForm


# --- CLIENTES ---

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})


def criar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/form_cliente.html', {'form': form})


def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/form_cliente.html', {'form': form})


def excluir_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'clientes/confirma_exclusao.html', {'objeto': cliente})


# --- PROJETOS ---

def lista_projetos(request):
    projetos = Projeto.objects.select_related('cliente').all()
    return render(request, 'clientes/lista_projetos.html', {'projetos': projetos})


def criar_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_projetos')
    else:
        form = ProjetoForm()
    return render(request, 'clientes/form_projeto.html', {'form': form})


def editar_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('lista_projetos')
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'clientes/form_projeto.html', {'form': form})


def excluir_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method == 'POST':
        projeto.delete()
        return redirect('lista_projetos')
    return render(request, 'clientes/confirma_exclusao.html', {'objeto': projeto})
