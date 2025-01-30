from django.views.generic import ListView,CreateView,DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import ProdutoForm
from .models import Produto

class ProdutoListView(ListView):
    model = Produto
    template_name = "produto_list.html"
    context_object_name = "produtos"

class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = "produto_form.html"
    success_url = reverse_lazy('produto_list')

class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = "produto_form.html"
    success_url = reverse_lazy('roduto_list')

class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = "produto_confirm_delet.html"
    success_url = reverse_lazy('produto_list')