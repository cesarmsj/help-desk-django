# Generated by Django 3.2.4 on 2021-06-24 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0006_remove_chamado_interacao_teste'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chamado_interacao',
            old_name='data_abertura',
            new_name='data_interacao',
        ),
        migrations.RenameField(
            model_name='chamado_interacao',
            old_name='descricao',
            new_name='interacao',
        ),
        migrations.RemoveField(
            model_name='chamado_interacao',
            name='data_fechamento',
        ),
    ]
