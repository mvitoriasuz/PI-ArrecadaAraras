from django.contrib.auth.backends import BaseBackend
from .services import LogarUsuarioService
from django.contrib.auth.models import User

class MongoBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        logar_service = LogarUsuarioService()
        if logar_service.validar_credenciais(username, password):
            try:
                user = User.objects.get(username=username)
                return user
            except User.DoesNotExist:
                user = User(username=username)
                user.set_password(password)
                user.save()
                return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
