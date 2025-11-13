from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages 
from .models import Equipamento
from .forms import EquipamentoForm
from .models import Cep
from .models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User # Importa o modelo User
from django.contrib.auth.decorators import login_required # Importa o decorador de login
from django.contrib.auth import logout
from django.core.paginator import Paginator
from django.http import HttpResponse





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

# Editar equipamento
def editar_equipamento(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        form = EquipamentoForm(request.POST, instance=equipamento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipamento atualizado com sucesso!')
            return redirect('listar_equipamentos')
    else:
        form = EquipamentoForm(instance=equipamento)
    return render(request, 'equipamentos/editar.html', {'form': form, 'equipamento': equipamento})

# Excluir (desativar) equipamento
def excluir_equipamento(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk) 
    equipamento.ativo = False
    equipamento.save()
    messages.warning(request, 'Equipamento movido para a lista de excluídos.')
    return redirect('listar_equipamentos')

# Listar equipamentos excluídos
@login_required
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

# Listar equipamentos ativos 
def listar_equipamentos(request):
    equipamentos = Equipamento.objects.filter(ativo=True)
    paginator = Paginator(equipamentos, 4)  # 2 por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'equipamentos/listar.html', {
        'page_obj': page_obj,
        'total': equipamentos.count()
    })

# Deletar equipamento permanentemente
def delete_equipamento(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    equipamento.delete()
    messages.warning(request, 'Equipamento excluído permanentemente.')
    return redirect('listar_excluidos')


# Página de login 
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('listar_equipamentos')  # vai pra lista se o login for ok
        else:
            return render(request, 'equipamentos/login.html', {'error': 'Nome de usuário ou senha inválidos.'})
    return render(request, 'equipamentos/login.html')

# Página de cadastro 
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        cep = request.POST.get("cep")
        endereco = request.POST.get("endereco")
        bairro = request.POST.get("bairro")
        cidade = request.POST.get("cidade")
        estado = request.POST.get("estado")
        tem_equipamento = request.POST.get("tem_equipamento") == "on"

        if password1 != password2:
            messages.error(request, "As senhas não coincidem.")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error (request, "Usuário já existe.")
            return redirect("register")

# Criar usuário
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

 # Criar perfil associado ao usuário/cadastro
        Cep.objects.create(
            user=user,
            cep=cep,
            endereco=endereco,
            bairro=bairro,
            cidade=cidade,
            estado=estado,
            tem_equipamento=tem_equipamento
        )

        messages.success(request, "Usuário cadastrado com sucesso! Faça login.")
        return redirect("login")

    return render(request, "equipamentos/register.html")
   

# Sair do sistema
def logout_view(request):
    logout(request)
    return redirect("login")
    
# Página do perfil do usuário
def user_profile(request):
    user_profile = User.objects.get(username=request.user.username)
    cep_profile = Cep.objects.get(user=user_profile)    
    return render(request, "equipamentos/user.html")
