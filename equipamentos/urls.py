from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_equipamentos, name='listar_equipamentos'),
    path('adicionar/', views.adicionar_equipamento, name='adicionar_equipamento'),
    path('adicionar2/', views.adicionar_equipamento2, name='adicionar_equipamento2'),
    path('editar/<int:pk>/', views.editar_equipamento, name='editar_equipamento'),
    path('excluir/<int:pk>/', views.excluir_equipamento, name='excluir_equipamento'),
    path('excluidos/', views.listar_excluidos, name='listar_excluidos'),
    path('restaurar/<int:pk>/', views.restaurar_equipamento, name='restaurar_equipamento'), # Estava faltando essa linha pra lista de excluidos funcionar 
    path('delete/<int:pk>/', views.delete_equipamento, name='delete_equipamento')
]
