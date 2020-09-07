from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Lote(models.Model):
    
    class Meta:
        db_table = 'lote' 

    nome = models.CharField(max_length=80)
    dt_fabric = models.DateField(auto_now=True)
    quantidade = models.IntegerField()

    def __str__(self):
        return '%d: %s' % (self.id, self.nome)

class Item(models.Model):

    class Meta:
        db_table = 'item'

    lote = models.ForeignKey(Lote, on_delete=models.CASCADE)
    nome = models.CharField(max_length=80)
    descricao = models.CharField(max_length=200)
    cor = models.CharField(max_length=40)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return '%d: %s' % (self.id, self.nome)

class Cliente(models.Model):

    class Meta:
        db_table = 'cliente'

    cpf = models.CharField(max_length=14)
    nome = models.CharField(max_length=80)
    dt_nasc = models.DateField()
    
    def __str__(self):
        return '%d: %s' % (self.id, self.nome)

# class Vendedor(models.Model):

#     class Meta:
#         db_table = 'vendedor'

#     cpf = models.CharField(max_length=14)
#     nome = models.CharField(max_length=80)

#     def __str__(self):
#         return '%d: %s' % (self.id, self.nome)

class Vendedor(AbstractUser):
    pass

    def __str__(self):
        return self.username

class Pedido(models.Model):

    class Meta:
        db_table = 'pedido'

    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    itens = models.ManyToManyField('Item')
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    dt_compra = models.DateField(auto_now=True)

    def __str__(self):
        return '%d' % (self.id)
