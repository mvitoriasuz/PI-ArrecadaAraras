from django.urls import path
from.views import cadastro, index  # Certifique-se de que o caminho de importação esteja correto

app_name = 'core'

urlpatterns = [
    path('', index, name='index'), 
    path('Cadastro/', cadastro, name='cadastro'),
]
