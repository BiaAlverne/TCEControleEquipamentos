from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Equipamento
from .forms import EquipamentoForm

# Listar equipamentos ativos
def listar_equipamentos(request):
    equipamentos = Equipamento.objects.filter(ativo=True)
    return render(request, 'equipamentos/listar.html', {'equipamentos': equipamentos})

# Listar equipamentos excluídos
def equipamentos_excluidos(request):
    equipamentos = Equipamento.objects.filter(ativo=False)
    return render(request, 'equipamentos/excluidos.html', {'equipamentos': equipamentos})

# Adicionar novo equipamento/usuário/setor
def adicionar_equipamento(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        tipo = request.POST.get('tipo')
        numero_patrimonio = request.POST.get('numero_patrimonio')
        setor = request.POST.get('setor')
        usuario_atual = request.POST.get('usuario_atual')
        Equipamento.objects.create(nome=nome, tipo=tipo, numero_patrimonio=numero_patrimonio, setor=setor, usuario_atual=usuario_atual)
        return redirect('listar_equipamentos')
    return render(request, 'equipamentos/adicionar.html')


# Excluir (desativar) equipamento
def excluir_equipamento(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    equipamento.ativo = False
    equipamento.save()
    messages.warning(request, 'Equipamento movido para a lista de excluídos.')
    return redirect('listar_equipamentos')

# Listar equipamentos excluídos
def listar_excluidos(request):
    equipamentos_excluidos = Equipamento.objects.filter(ativo=False)
    return render(request, 'equipamentos/excluidos.html', {'equipamentos': equipamentos_excluidos})

# Restaurar equipamento
def restaurar_equipamento(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    equipamento.ativo = True
    equipamento.save()
    messages.success(request, 'Equipamento restaurado com sucesso!')
    return redirect('equipamentos_excluidos')
