# Generated by Django 3.2.4 on 2021-06-23 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Atendente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='atendente', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Chamado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('A', 'Aberto'), ('E', 'Em Andamento'), ('F', 'Finalizado')], max_length=1)),
                ('data_abertura', models.DateTimeField(blank=True)),
                ('data_fechamento', models.DateTimeField(blank=True, null=True)),
                ('fk_atendente', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='helpdesk.atendente')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Chamado_Interacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
                ('data_abertura', models.DateTimeField(blank=True)),
                ('data_fechamento', models.DateTimeField(blank=True, null=True)),
                ('teste', models.CharField(max_length=200)),
                ('fk_chamado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helpdesk.chamado')),
            ],
        ),
        migrations.AddField(
            model_name='chamado',
            name='fk_cliente',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='helpdesk.cliente'),
        ),
    ]