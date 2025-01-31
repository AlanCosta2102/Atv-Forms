from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('produtos/', views.ProdutoListView.as_view(), name='produto_list'),
    path('produtos/novo/', views.ProdutoCreateView.as_view(), name='create_produto'),
    path('produtos/editar/<int:pk>/', views.ProdutoUpdateView.as_view(), name='produto_update'),
    path('produtos/deletar/<int:pk>/', views.ProdutoDeleteView.as_view(), name='produto_delete'),
]
