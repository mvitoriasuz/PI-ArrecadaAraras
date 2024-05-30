from django.db import models

class CadastroModel(models.Model):
    nome = models.CharField('Nome', max_length=200)
    cpf = models.CharField('CPF', max_length=14)
    email = models.EmailField('email')
    senha = models.CharField('senha', max_length=50)
    data_nasc = models.DateField('data_nasc')

    def __str__(self):
        return self.nome

