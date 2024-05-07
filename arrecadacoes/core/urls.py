from django.urls import path
from core import views

urlpatterns = [
    path('', views.cadastro_home, name='home'),
    path('Cadastro/', views.cadastro, name='cadastro'),
]