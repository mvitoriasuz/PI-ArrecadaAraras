# Generated by Django 5.0.4 on 2024-06-13 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_ong_endereco_ong_horario_funcionamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='doacao',
            name='tipo_doacao',
            field=models.CharField(blank=True, max_length=100, verbose_name='Tipo de Doação'),
        ),
    ]
