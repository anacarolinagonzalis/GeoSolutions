from django import forms
from .models import Cliente, Projeto


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cnpj_cpf', 'email', 'telefone', 'endereco']


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['cliente', 'titulo', 'tipo_servico', 'status', 'data_inicio', 'prazo_vencimento', 'responsavel']
