from django import forms
from .models import Produto, Categoria, Fornecedor

class ProdutoForm(forms.Form):
    nome = forms.CharField(label="Nome do Produto", max_length=100)
    descricao = forms.CharField(label="Descrição", widget=forms.Textarea, required=False)
    preco = forms.DecimalField(label="Preço", max_digits=10, decimal_places=2)
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), label="Categoria")
    fornecedor = forms.ModelMultipleChoiceField(
        queryset=Fornecedor.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Fornecedores"
    )
