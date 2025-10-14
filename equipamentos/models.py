# models.py
from django.db import models

class Equipamento(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    numero_patrimonio = models.CharField(max_length=30, unique=True)
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
    ativo = models.BooleanField(default=True) 

    def __str__(self):
        return f"{self.nome} ({self.numero_patrimonio})"


class Movimentacao(models.Model):
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    data_movimentacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.equipamento.nome} - {self.origem} → {self.destino}"
