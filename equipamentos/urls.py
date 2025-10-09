from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_equipamentos, name='listar_equipamentos'),
    path('excluir/<int:id>/', views.excluir_equipamento, name='excluir_equipamento'),
    path('excluidos/', views.listar_excluidos, name='listar_excluidos'),
    path('restaurar/<int:id>/', views.restaurar_equipamento, name='restaurar_equipamento'),
]
