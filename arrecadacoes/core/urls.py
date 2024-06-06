from django.urls import path
from.views import index, cadastro_view, login_view 

app_name = 'core'

urlpatterns = [
    path('', index, name='index'), 
    path('Cadastro/', cadastro_view, name='cadastro'),
    path('Login/', login_view, name='login'), 
]
