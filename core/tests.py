from django.test import TestCase, Client
from django.urls import reverse
from.forms import CadastroForm
from.models import CadastroModel

class CadastroViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.valid_payload = {
            'nome': 'João Silva',
            'cpf': '12345678901',
            'email': 'joao.silva@example.com',
            'senha': 'senha123',
            'data_nasc': '1990-01-01'
        }
        self.invalid_payload = {}

    def test_cadastro_view_success(self):
        response = self.client.post(reverse('cadastro'), data=self.valid_payload)
        self.assertEqual(response.status_code, 302)  # Redirecionamento após o cadastro bem-sucedido
        self.assertTrue(CadastroModel.objects.exists())  # Verifica se o usuário foi criado

    def test_cadastro_view_failure(self):
        response = self.client.post(reverse('cadastro'), data=self.invalid_payload)
        self.assertEqual(response.status_code, 200)  # Status code 200 indica uma resposta bem-sucedida, mas sem redirecionamento
        self.assertFalse(CadastroModel.objects.exists())  # Verifica se o usuário não foi criado

class LoginViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CadastroModel.objects.create_user(
            email='joao.silva@example.com',
            password='senha123',
            nome='João Silva'
        )

    def test_login_view_success(self):
        response = self.client.post(reverse('login'), data={
            'email': 'joao.silva@example.com',
            'password': 'senha123'
        })
        self.assertEqual(response.status_code, 302)  # Redirecionamento após o login bem-sucedido
        self.assertTrue(self.client.session.get('_auth_user_id'))  # Verifica se a sessão do usuário foi iniciada

    def test_login_view_failure(self):
        response = self.client.post(reverse('login'), data={
            'email': 'invalid@email.com',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)  # Status code 200 indica uma resposta bem-sucedida, mas sem redirecionamento
        self.assertFalse(self.client.session.get('_auth_user_id'))  # Verifica se a sessão do usuário não foi iniciada
