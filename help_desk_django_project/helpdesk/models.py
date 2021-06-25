from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class BaseModel(models.Model):
    objects = models.Manager()
    class Meta:
        abstract = True

class Cliente(BaseModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        default=1,
    )
    class Meta:
        managed: False
        db_table = 'helpdesk_cliente'

class Atendente(BaseModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        default=1,
    )

    class Meta:
        managed: False
        db_table = 'helpdesk_atendente'

class Chamado(BaseModel):

    STATUS = (
        ('A', 'Aberto'),
        ('E', 'Em Andamento'),
        ('F', 'Finalizado')
    )

    descricao = models.CharField(max_length=200)
    status = models.CharField(max_length=1, choices=STATUS, default='A')
    fk_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
    fk_atendente = models.ForeignKey(Atendente, on_delete=models.CASCADE, null=True)
    data_abertura = models.DateTimeField(auto_now_add=True, blank=True)
    data_fechamento = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.descricao

class Chamado_Interacao(models.Model):

    fk_chamado = models.ForeignKey(Chamado, on_delete=models.CASCADE)
    interacao = models.CharField(max_length=200)
    data_interacao = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.descricao

