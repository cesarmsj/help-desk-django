from django.contrib.auth.models import User
from django.db import models

class Cliente(models.Model):
    user = models.OneToOneField(User, related_name='cliente', on_delete=models.CASCADE)

class Atendente(models.Model):
    user = models.OneToOneField(User, related_name='atendente', on_delete=models.CASCADE)

class Chamado(models.Model):

    STATUS = (
        ('A', 'Aberto'),
        ('E', 'Em Andamento'),
        ('F', 'Finalizado')
    )

    descricao = models.CharField(max_length=200)
    status = models.CharField(max_length=1, choices=STATUS)
    fk_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default='')
    fk_atendente = models.ForeignKey(Atendente, on_delete=models.CASCADE, default='')
    data_abertura = models.DateTimeField(blank=True)
    data_fechamento = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.descricao

class Chamado_Interacao(models.Model):

    fk_chamado = models.ForeignKey(Chamado, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    data_abertura = models.DateTimeField(blank=True)
    data_fechamento = models.DateTimeField(null=True, blank=True)
    teste = models.CharField(max_length=200)

