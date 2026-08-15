# membros/urls.py
from django.urls import path
from . import views

app_name = 'membros'

urlpatterns = [
    # Página inicial
    path('', views.home, name='home'),
    
    # Registro de usuário (mudei de cadastro para registro)
    path('registro/', views.registro, name='registro'),  # ← Mudei aqui
    
    # CRUD de Membros
    path('membros/', views.listar_membros, name='listar_membros'),
    path('membros/criar/', views.criar_membro, name='criar_membro'),
    path('membros/editar/<int:id>/', views.editar_membro, name='editar_membro'),
    path('membros/deletar/<int:id>/', views.deletar_membro, name='deletar_membro'),
]