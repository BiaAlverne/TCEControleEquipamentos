from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_equipamentos, name='listar_equipamentos'),
    path('novo/', views.criar_equipamento, name='criar_equipamento'),
    path('editar/<int:id>/', views.editar_equipamento, name='editar_equipamento'),
    path('excluir/<int:id>/', views.excluir_equipamento, name='excluir_equipamento'),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('equipamentos.urls')),
]
