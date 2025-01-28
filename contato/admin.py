from django.contrib import admin
from .models import Categoria, Fornecedor, Produto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome') 
    search_fields = ('nome',)  
    ordering = ('nome',)  


@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')  
    search_fields = ('nome', 'email')  
    ordering = ('nome',)  


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'categoria') 
    list_filter = ('categoria', 'fornecedor')  
    search_fields = ('nome', 'descricao')  
    ordering = ('nome',)  
