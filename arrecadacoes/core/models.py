from django.db import models

class CadastroModel(models.Model):
    nome = models.CharField('Nome', max_length=200)
    email = models.EmailField('Email')
    senha = models.CharField('Senha', max_length=50)

    def __str__(self):
        return self.nome
    
class Instituicao(models.Model):
    nome = models.CharField(max_length=100)
    chave_pix = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome
    
class Doacao(models.Model):
    ong_nome = models.CharField('Nome da ONG', max_length=100)
    item_doado = models.CharField('Item Doado', max_length=100, blank=True)
    descricao_doacao = models.TextField('Descrição da Doação', null=True, blank=True)
    data_doacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ong_nome} - {self.item_doado}"
