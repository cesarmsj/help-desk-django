from django.db import models


class Cliente(models.Model):

    username = models.CharField(max_length=20, default='')
    password = models.CharField(max_length=20, default='123456')
    nome = models.CharField(max_length=50)
    nascimento = models.DateField(null=True)
    email = models.EmailField()
    SEXOS = (
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )

    sexo = models.CharField(max_length=1, choices=SEXOS)
    cidade = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Atendente(models.Model):

    username = models.CharField(max_length=20, default='')
    password = models.CharField(max_length=20, default='123456')
    nome = models.CharField(max_length=50)
    nascimento = models.DateField()
    email = models.EmailField()
    SEXOS = (
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )

    sexo = models.CharField(max_length=1, choices=SEXOS)
    cidade = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Chamado(models.Model):

    STATUS = (
        ('A', 'Aberto'),
        ('E', 'Em Andamento'),
        ('F', 'Finalizado')
    )

    descricao = models.CharField(max_length=200)
    status = models.CharField(max_length=1, choices=STATUS)
    data_abertura = models.DateField()
    data_fechamento = models.DateField(null=True)
    fk_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fk_atendente = models.ForeignKey(Atendente, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

class Chamado_Interacao(models.Model):

    fk_chamado = models.ForeignKey(Chamado, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)

