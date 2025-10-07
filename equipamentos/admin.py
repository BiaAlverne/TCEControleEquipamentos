from django.contrib import admin
from .models import Equipamento, Movimentacao

class MovimentacaoInline(admin.TabularInline):
    model = Movimentacao
    extra = 1
    readonly_fields = ('data_movimentacao',)
    fields = ('origem', 'destino', 'data_movimentacao', 'observacao')
    show_change_link = True

@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'numero_patrimonio', 'status', 'setor', 'usuario_atual')
    search_fields = ('nome', 'numero_patrimonio', 'setor')
    list_filter = ('status', 'setor')
    inlines = [MovimentacaoInline]

@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ('equipamento', 'origem', 'destino', 'data_movimentacao')
    search_fields = ('equipamento__nome', 'origem', 'destino')
    list_filter = ('data_movimentacao',)
