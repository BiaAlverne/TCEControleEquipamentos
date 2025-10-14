from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_equipamentos, name='listar_equipamentos'),
    path('adicionar/', views.adicionar_equipamento, name='adicionar_equipamento'),
    path('excluir/<int:pk>/', views.excluir_equipamento, name='excluir_equipamento'),
    path('excluidos/', views.listar_excluidos, name='listar_excluidos'),
]
