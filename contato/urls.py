from django.urls import path
from .views import ProdutoListView,ProdutoDeleteView,ProdutoCreateView,ProdutoUpdateView

urlpatterns = [
    path('produtos/',ProdutoListView.as_view(),name='produto_list'),
    path('produtos/novo/',ProdutoCreateView.as_view(),name='produto_create'),
    path('produtos/editar/<int:pk>/',ProdutoUpdateView.as_view(),name='produto_update'),
    path('produtos/deletar/<int:pk>',ProdutoDeleteView.as_view(),name='produto_delete'),
    
]
