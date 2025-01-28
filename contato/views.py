from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ProdutoForm
from .models import Produto

def create_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = Produto()
            produto.nome = form.cleaned_data['nome']
            produto.descricao = form.cleaned_data['descricao']
            produto.preco = form.cleaned_data['preco']
            produto.categoria = form.cleaned_data['categoria']
            produto.save()
            produto.fornecedor.set(form.cleaned_data['fornecedor'])
            return redirect(reverse('index'))  
    else:
        form = ProdutoForm()

    return render(request, 'contato/create.html', {'form': form})


def index(request):
    return render(request, 'contato/index.html')
