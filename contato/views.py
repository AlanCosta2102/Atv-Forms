from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from django.urls import reverse_lazy
from .forms import ProdutoForm
from .models import Produto
from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.views.generic import TemplateView
from django.views import View
from django import forms
from django.contrib import messages
from django.urls import reverse

class ProdutoListView(ListView):
    model = Produto
    template_name = "produto_list.html"
    context_object_name = "produtos"
    paginate_by = 5

class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = "produto_form.html"
    success_url = reverse_lazy('produto_list')

class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = "produto_confirm_delete.html"
    success_url = reverse_lazy('produto_list')
    
class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = "produto_form.html"
    success_url = reverse_lazy('produto_list')
    
def home(request):
    return render(request, 'home.html')

def get_queryset(self):
    queryset = Produto.objects.all()
    nome = self.request.GET.get('nome', '').strip()
    preco_min = self.request.GET.get('preco_min')
    preco_max = self.request.GET.get('preco_max')

    if nome:
        queryset = queryset.filter(nome__icontains=nome)

    try:
        if preco_min:
            preco_min = float(preco_min)
            queryset = queryset.filter(preco__gte=preco_min)
        
        if preco_max:
            preco_max = float(preco_max)
            queryset = queryset.filter(preco__lte=preco_max)
    except ValueError:
        pass  
    return queryset

class DashboardView(TemplateView):
    template_name = 'dashboard.html'
    

class CriarProdutoView(View):
    def get(self, request):
        form = ProdutoForm()
        return render(request, 'produto_form.html', {'form': form})

    def post(self, request):
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto cadastrado com sucesso!")  
            return redirect('produto_list')  
        return render(request, 'produto_form.html', {'form': form})


class ProdutoForm(forms.ModelForm):
    class Meta:
        model  =Produto
        fields = ['nome','codigo','preco','quantidade_estoque','imagem']