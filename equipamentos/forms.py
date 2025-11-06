from django import forms
from .models import Equipamento

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['nome', 'tipo', 'numero_patrimonio', 'status', 'setor', 'usuario_atual', 'observacao']
        widgets = {
            'observacao': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super(EquipamentoForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['numero_patrimonio'].widget.attrs['readonly'] = True

    def clean_numero_patrimonio(self):
        numero_patrimonio = self.cleaned_data.get('numero_patrimonio')
        if self.instance and self.instance.pk:
            pass
        elif Equipamento.objects.filter(numero_patrimonio=numero_patrimonio).exists():
            raise forms.ValidationError("O número de patrimômio não pode ser repetido, mesmo que já esteja excluído!")
        return numero_patrimonio
    
'''
Class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereço
        fields = ['rua', 'cidade', 'estado', 'cep']
    '''
