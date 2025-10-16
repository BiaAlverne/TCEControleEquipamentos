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
        status = request.POST.get('status') 
        setor = request.POST.get('setor')
        usuario_atual = request.POST.get('usuario_atual')
       

        # Verifica se já existe um equipamento ativo com esse tombo
        if Equipamento.objects.filter(numero_patrimonio=numero_patrimonio).exists(): # Foi retirado o ativo=true 
            messages.warning(request, 'O número de patrimômio não pode ser repetido, mesmo que já esteja excluído!')
            return redirect('adicionar_equipamento')

        # Cria o novo equipamento se não houver duplicidade de tombo
        Equipamento.objects.create(
            nome=nome,
            tipo=tipo,
            numero_patrimonio=numero_patrimonio,
            status=status,
            setor=setor,
            usuario_atual=usuario_atual
            
        )

        messages.success(request, 'Equipamento adicionado com sucesso!')
        return redirect('listar_equipamentos')

    return render(request, 'equipamentos/adicionar.html')

# Adicionar equipamento usando ModelForm
def adicionar_equipamento2(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipamento adicionado com sucesso!')
            return redirect('listar_equipamentos')
         #foi retirado o else com mensagem de erro, pq o próprio form já faz isso
    else:
        form = EquipamentoForm()
    return render(request, 'equipamentos/adicionar2.html', {'form': form} ) 


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
    return redirect('listar_excluidos')
