# Ferramentas para mostrar páginas e redirecionar
from django.shortcuts import render, redirect, get_object_or_404
 # Pegamos nosso modelo (o caderno)
  from .models import Membros 
# Pegamos nosso formulário (a ficha)
 from .forms import MembrosForm 
# VIEW 1: MOSTRAR A LISTA DE MEMBROS 
# Esta função é como abrir o caderno e ler todos os nomes
 def listar_membros(request): 
  # Pega TODOS os membros do banco de dados 
   .all() = todos
 # .order_by('firstname') = ordena por nome 
  lista = Membros.objects.all().order_by('firstname')
  # Mostra a página com a lista 
  # Render = "mostrar" 
  # 'meuprimeiro.html' = qual página mostrar 
  # {"membros": lista} = enviar a lista para a página
   return render(request, "meuprimeiro.html", {"membros": lista}) 
# VIEW 2: CRIAR UM NOVO MEMBRO
 # Esta função é como adicionar uma nova ficha no caderno
  def criar_membro(request): 
 # VERIFICA se o usuário enviou o formulário
  # POST = quando o usuário clica em "Salvar" 
  if request.method == "POST":
     # Pega os dados do formulário 
     form = MembrosForm(request.POST)
      # Verifica se os dados estão certos
      if form.is_valid():
        # Salva no banco de dados
        form.save() 
        # Volta para a lista de membros
        return redirect('listar_membros') 
     else: 
# Se é a primeira vez, mostra o formulário vazio
 form = MembrosForm()
 # Mostra a página do formulário
  return render(request, "criar_membro.html", {"form": form}) 
# VIEW 3: EDITAR UM MEMBRO 
# Esta função é como pegar uma ficha e trocar informações 
def editar_membro(request, id): 
# Procura o membro pelo ID (número de identificação)
 # get_object_or_404 = "procura ou mostra erro 404 se não achar"
  membro = get_object_or_404(Membros, id=id) 
# Verifica se o usuário enviou o formulário 
if request.method == "POST": 
  # Pega os dados do formulário e coloca no membro
   form = MembrosForm(request.POST, instance=membro) 
   # Verifica se os dados estão certos 
   if form.is_valid(): 
     # Salva as mudanças no banco de dados
      form.save() 
      # Volta para a lista de membros 
      return redirect('listar_membros') 
   else:
      # Mostra o formulário com os dados do membro 
      form = MembrosForm(instance=membro) 
      # Mostra a página de edição 
      return render(request, "editar_membro.html", {"form": form, "membr o": membro}) 
   # VIEW 4: DELETAR UM MEMBRO 
   # Esta função é como rasgar uma ficha do caderno 
   def deletar_membro(request, id): 
     #Procura o membro pelo ID 
     membro = get_object_or_404(Membros, id=id)
     # Verifica se o usuário confirmou a exclusão
     if request.method == "POST":
    # Apaga o membro do banco de dados
    #membro.delete() 
    # Volta para a lista de membros
    return redirect('listar_membros')
 # Mostra a página de confirmação
 return render(request, "confirmar_delecao.html", {"membro": membro}