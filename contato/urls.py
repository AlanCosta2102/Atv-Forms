from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .views import ProdutoListView
urlpatterns = [
    path('', views.home, name='home'),  
    path('produtos/', views.ProdutoListView.as_view(), name='produto_list'),
    path('produtos/novo/', views.ProdutoCreateView.as_view(), name='create_produto'),
    path('produtos/editar/<int:pk>/', views.ProdutoUpdateView.as_view(), name='produto_update'),
    path('produtos/deletar/<int:pk>/', views.ProdutoDeleteView.as_view(), name='produto_delete'),
    path('login/',auth_views.LoginView.as_view(template_name = 'login.html')),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
    path('dashboard/',login_required(views.DashboardView.as_view()),name='dashboard'),

    path('produtos/',login_required(views.ProdutoListView.as_view()),name='produtos'),
    path('produto/novo/', login_required(views.ProdutoCreateView.as_view()),name='produto_novo'),
]
