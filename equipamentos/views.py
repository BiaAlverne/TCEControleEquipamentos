from django.shortcuts import render, redirect
from .models import Equipamento

def listar_equipamentos(request):
    equipamentos = Equipamento.objects.all()
    return render(request, 'equipamentos/listar.html', {'equipamentos': equipamentos})

def criar_equipamento(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        # Salva no banco
        Equipamento.objects.create(nome=nome, descricao=descricao)
        return redirect('listar_equipamentos')

    return render(request, 'equipamentos/form.html')
