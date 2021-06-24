from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Cliente(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        default=''
    )

    class Meta:
        managed: False
        db_table = 'helpdesk_cliente'

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Cliente.objects.create(user=instance)
    instance.cliente.save()

class Atendente(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        default=''
    )

    class Meta:
        managed: False
        db_table = 'helpdesk_atendente'

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
    data_abertura = models.DateTimeField(auto_now_add=True, blank=True)
    data_fechamento = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.descricao

class Chamado_Interacao(models.Model):

    fk_chamado = models.ForeignKey(Chamado, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    data_abertura = models.DateTimeField(auto_now_add=True, blank=True)
    data_fechamento = models.DateTimeField(null=True, blank=True)
    teste = models.CharField(max_length=200)

    def __str__(self):
        return self.descricao

