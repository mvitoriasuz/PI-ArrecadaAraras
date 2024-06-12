from pymongo import MongoClient
from datetime import datetime
from typing import List, Dict, Any
from django.contrib.auth.models import User

class CadastroClienteService:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["arrecadacoes"]
        self.collection = self.db["doacao_ong"]

    def cadastrar_cliente(
        self, nome: str, cpf: str, email: str, senha: str, data_nasc: str
    ) -> dict:
        try:
            user = User(
                email=email,
                username=nome,
                password=senha,
            )
            user.save()
            documento = {
                "nome": nome,
                "cpf": cpf,
                "email": email,
                "senha": senha,
                "data_nasc": data_nasc,
                "ong_id": None,
                "descricao_doacao": None,
                "data_doacao": None,
                "user_id": user.id,
            }
            self.collection.insert_one(documento)
            return {"success": "Cliente cadastrado com sucesso."}
        except Exception as e:
            return {"error": str(e)}


class LogarUsuarioService:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["arrecadacoes"]
        self.collection = self.db["doacao_ong"]

    def validar_credenciais(self, email: str, senha: str) -> bool:
        usuario = self.collection.find_one({"email": email, "senha": senha})
        print(f"Usuário encontrado: {usuario}")  # Para depuração
        return usuario is not None

    def login(self, email: str, senha: str):
        return self.collection.find_one({"email": email, "senha": senha})

    def fazer_doacao(self, cliente_id: str, ong_id: str, descricao_doacao: str) -> dict:
        try:
            self.collection.update_one(
                {"_id": cliente_id},
                {
                    "$set": {
                        "ong_id": ong_id,
                        "descricao_doacao": descricao_doacao,
                        "data_doacao": datetime.now(),
                    }
                },
            )
            return {"success": "Doação registrada com sucesso."}
        except Exception as e:
            return {"error": str(e)}

    def listar_clientes(self) -> List[Dict[str, Any]]:
        clientes = self.collection.find({}, {"_id": 0, "senha": 0})
        return list(clientes)
