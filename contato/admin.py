from django.contrib import admin
from .models import Produto, Categoria, Fornecedor

admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Fornecedor)
