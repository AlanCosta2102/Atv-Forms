from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from django.urls import reverse_lazy
from .forms import ProdutoForm
from .models import Produto
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import TemplateView

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
        nome = self.request.GET.get('nome')
        preco_min = self.request.GET.get('preco_min')
        preco_max = self.request.GET.get('preco_max')

        if nome:
            queryset = queryset.filter(nome__icontains=nome)

        if preco_min:
            queryset = queryset.filter(preco__gte=preco_min)

        if preco_max:
            queryset = queryset.filter(preco__lte=preco_max)

        return queryset


class DashboardView(TemplateView):
    template_name = 'dashboard.html'