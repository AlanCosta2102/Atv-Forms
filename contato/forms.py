from django import forms
from .models import Produto

class ProdutoForm(forms.Form):
   class Meta:
      model = Produto
      fields = ['nome','descricao','preco','quantidade_estoque','codigo','categoria','fornecedor']

def clean_nome(self):
   nome = self.clean_data.get('nome')
   if len(nome) < 3:
      raise forms.ValidationError('O nome do produto deve conter pelo menos 3 caracteres')
   return nome

def clean_preco(self):
   preco = self.clean_data.get('preco')
   if preco <=0:
      raise forms.ValidationError('O preço deve ser maior ou igual a zero')
   return preco