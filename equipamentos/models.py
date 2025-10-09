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
        default='disponível'
    )
    setor = models.CharField(max_length=100)
    usuario_atual = models.CharField(max_length=100, blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)
    ativo = models.BooleanField(default=True)  # 🔹 usado pra "excluir" sem apagar

    def __str__(self):
        return f"{self.nome} ({self.numero_patrimonio})"
