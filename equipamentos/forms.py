from django import forms
from .models import Equipamento

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['nome', 'tipo', 'numero_patrimonio', 'status', 'setor', 'usuario_atual', 'observacao']
        widgets = {
            'observacao': forms.Textarea(attrs={'rows': 3}),
        }
    
    def clean_numero_patrimonio(self):
        numero_patrimonio = self.cleaned_data.get('numero_patrimonio')
        if Equipamento.objects.filter(numero_patrimonio=numero_patrimonio).exists():
            raise forms.ValidationError("O número de patrimômio não pode ser repetido, mesmo que já esteja excluído!")
        return numero_patrimonio
    
    
