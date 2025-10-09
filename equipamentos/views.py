from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Equipamento

def listar_equipamentos(request):
    equipamentos = Equipamento.objects.filter(ativo=True)
    return render(request, 'equipamentos/listar.html', {'equipamentos': equipamentos})

def excluir_equipamento(request, id):
    equipamento = get_object_or_404(Equipamento, id=id)
    equipamento.ativo = False
    equipamento.save()
    messages.warning(request, f"Equipamento '{equipamento.nome}' movido para a lixeira.")
    return redirect('listar_equipamentos')

def listar_excluidos(request):
    equipamentos = Equipamento.objects.filter(ativo=False)
    return render(request, 'equipamentos/excluidos.html', {'equipamentos': equipamentos})

def restaurar_equipamento(request, id):
    equipamento = get_object_or_404(Equipamento, id=id)
    equipamento.ativo = True
    equipamento.save()
    messages.success(request, f"Equipamento '{equipamento.nome}' foi restaurado com sucesso!")
    return redirect('listar_excluidos')
