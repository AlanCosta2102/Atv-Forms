from django import forms
from .models import Produto, Categoria, Fornecedor

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'quantidade_estoque', 'codigo', 'categoria', 'fornecedor']

    nome = forms.CharField(label="Nome do Produto")
    preco = forms.DecimalField(label="Preço")
    quantidade_estoque = forms.IntegerField(label="Quantidade em Estoque")
    codigo = forms.CharField(label="Código do Produto")
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), label="Categoria")
    fornecedor = forms.ModelMultipleChoiceField(queryset=Fornecedor.objects.all(), label="Fornecedor")
