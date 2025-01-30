from django.db import models
from django.core.validators import MinValueValidator,RegexValidator

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(
        max_length=100,
        validators=[RegexValidator(regex=r'^\w(3,)$',message="O nome deve ter pelo menos 3 caracteres e não conter caracteres especiais")]
    )
    descricao = models.TextField(blank=True)
    preco = models.DecimalField
    max_digits=10, 
    decimal_places=2,
    validators = [MinValueValidator(0.01,message="O preço deve ser maior que zero")]               
    quantidade_estoque =  models.PositiveIntegerField(
        validators = MinValueValidator(0,message="A quantidade de estoque deve ser igual o maior que zero")
    )
    codigo = models.CharField(
        max_length = 50,
        unique = True,
        validators = [RegexValidator(regex=r'^[a-zA-Z0-9]+$',message="O codigo deve conter apenas letras e numeros")]
    )
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="produtos")
    fornecedor = models.ManyToManyField(Fornecedor, related_name="produtos")

    def __str__(self):
        return self.nome
