from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('ongs/', views.ongs_view, name='ongs'),
    path('login/', views.login_view, name='login'),
    path('fazer_doacao/', views.fazer_doacao, name='fazer_doacao'),  # Adicionando a URL para processamento de doação
]