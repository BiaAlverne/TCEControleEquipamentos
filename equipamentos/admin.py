from django.contrib import admin
from .models import Equipamento, Movimentacao

@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'numero_patrimonio', 'status', 'setor', 'usuario_atual', 'ativo')
    list_filter = ('status', 'setor', 'ativo')
    search_fields = ('nome', 'numero_patrimonio', 'usuario_atual')


@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ('equipamento', 'origem', 'destino', 'data_movimentacao')
    list_filter = ('data_movimentacao',)
