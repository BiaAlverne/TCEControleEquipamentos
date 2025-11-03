from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/', include('django.contrib.auth.urls')),  # rotas padrão de autenticação do Django
    path('equipamentos/', include('equipamentos.urls')),
    path('', lambda request: redirect('equipamentos/login')),  # URL PRINCIPAL
]
