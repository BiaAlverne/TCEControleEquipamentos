from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_equipamentos, name='listar_equipamentos'),
    path('criar/', views.criar_equipamento, name='criar_equipamento'),
]
