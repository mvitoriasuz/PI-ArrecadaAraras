from django.db import models
from django.contrib.auth.models import User 

class CadastroModel(models.Model):
    nome = models.CharField('Nome', max_length=200)
    cpf = models.CharField('CPF', max_length=14)
    email = models.EmailField('email')
    senha = models.CharField('senha', max_length=50)
    data_nasc = models.DateField('data_nasc')

    def __str__(self):
        return self.nome
    
class Instituicao(models.Model):
    nome = models.CharField(max_length=100)
    chave_pix = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome

class Doacao(models.Model):
    donante = models.ForeignKey(User, on_delete=models.CASCADE)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    data_doacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.donante.username} - {self.instituicao.nome}"
