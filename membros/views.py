# Ferramentas para mostrar páginas e redirecionar
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Pegamos nosso formulário (a ficha)
from .forms import MembrosForm

# Pegamos nosso modelo (o caderno)
from .models import Membros


# VIEW DA PÁGINA INICIAL (INDEX)
def home(request):
    return render(request, "index.html")


# VIEW DE REGISTRO DE USUÁRIO (NOVA)
def registro(request):  # ← Mudei de cadastro para registro
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada para {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "registro.html", {"form": form})  # ← Mudei o template


# VIEW 1: MOSTRAR A LISTA DE MEMBROS
def listar_membros(request):
    lista = Membros.objects.all().order_by('firstname')
    return render(request, "meuprimeiro.html", {"membros": lista})


# VIEW 2: CRIAR UM NOVO MEMBRO
def criar_membro(request):
    if request.method == "POST":
        form = MembrosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_membros')
    else:
        form = MembrosForm()
    return render(request, "criar_membro.html", {"form": form})


# VIEW 3: EDITAR UM MEMBRO
def editar_membro(request, id):
    membro = get_object_or_404(Membros, id=id)
    if request.method == "POST":
        form = MembrosForm(request.POST, instance=membro)
        if form.is_valid():
            form.save()
            return redirect('listar_membros')
    else:
        form = MembrosForm(instance=membro)
    return render(request, "editar_membro.html", {"form": form, "membro": membro})


# VIEW 4: DELETAR UM MEMBRO
def deletar_membro(request, id):
    membro = get_object_or_404(Membros, id=id)
    if request.method == "POST":
        membro.delete()
        return redirect('listar_membros')
    return render(request, "confirmar_delecao.html", {"membro": membro})