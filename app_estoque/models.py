from django.db import models

class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    categoria = models.TextField(max_length=255)
    quantidade = models.IntegerField()
    preco = models.IntegerField()