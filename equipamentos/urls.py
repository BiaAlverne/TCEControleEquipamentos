from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_equipamentos, name='listar_equipamentos'),
    path('adicionar/', views.adicionar_equipamento, name='adicionar_equipamento'),
    path('adicionar2/', views.adicionar_equipamento2, name='adicionar_equipamento2'),
    path('excluir/<int:pk>/', views.excluir_equipamento, name='excluir_equipamento'),
    path('excluidos/', views.listar_excluidos, name='listar_excluidos'),
]
