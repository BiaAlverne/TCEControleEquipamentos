from django.db import models
from django.contrib.auth.models import User



class Equipamento(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    numero_patrimonio = models.CharField(max_length=30, unique=True) # Não aceita tombo duplicado
    status = models.CharField(
        max_length=20,
        choices=[
            ('disponível', 'Disponível'),
            ('em uso', 'Em uso'),
            ('manutenção', 'Manutenção'),
            
        ],
        default='disponível' #PADRÃO
    )
    setor = models.CharField(max_length=100)
    usuario_atual = models.CharField(max_length=100, blank=True, null=True)
    observacao = models.TextField(blank=True, null=True) 
    ativo = models.BooleanField (default=True)  # Campo para marcar se o equipamento está ativo ou excluído

    def __str__(self):
        return f"{self.nome} ({self.numero_patrimonio})"


class Movimentacao(models.Model):
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    data_movimentacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.equipamento.nome} - {self.origem} → {self.destino}"
    
class Cep (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    cep = models.CharField(max_length=9, blank=True)
    endereco = models.CharField(max_length=200, blank=True)
    bairro = models.CharField(max_length=100, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=2, blank=True)

    tem_equipamento = models.BooleanField(default=False)

    def __str__(self):
        return f"Cep de {self.user.username}"
    

