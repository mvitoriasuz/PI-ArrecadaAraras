from django.db import models

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
    ong_nome = models.CharField('Nome da ONG', max_length=100, null=True, blank=True)
    item_doado = models.CharField('Item Doado', max_length=100, null=True, blank=True)
    quantidade_doada = models.PositiveIntegerField('Quantidade Doada', null=True, blank=True)
    data_doacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.donante.username} - {self.ong_nome}"