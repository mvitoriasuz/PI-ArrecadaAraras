# Generated by Django 5.0.4 on 2024-06-13 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_ong_informacoes_adicionais_ong_tipo_doacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDoacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
    ]