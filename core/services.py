from pymongo import MongoClient
from datetime import datetime
from typing import List, Dict, Any
from .models import Cliente
from datetime import datetime

class CadastroClienteService:
    def cadastrar_cliente(
        self, nome: str, email: str, senha: str,) -> dict:
        try:
            cliente = Cliente.objects.create(
                nome=nome,
                email=email,
                senha=senha,
            )
            return {"success": "Cliente cadastrado com sucesso."}
        except Exception as e:
            return {"error": str(e)}
        
        
class LogarUsuarioService:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["arrecadacoes"]
        self.collection = self.db["doacao_ong"]

    def fazer_doacao(self, cliente_id: str, ong_nome: str, descricao_doacao: str) -> dict:
        try:
            self.collection.insert_one({
                "cliente_id": cliente_id,
                "ong_nome": ong_nome,
                "descricao_doacao": descricao_doacao,
                "data_doacao": datetime.now()
            })
            return {"success": "Doação registrada com sucesso."}
        except Exception as e:
            return {"error": str(e)}

    def listar_doacoes(self, cliente_id: str) -> List[Dict[str, Any]]:
        doacoes = self.collection.find({"cliente_id": cliente_id})
        return list(doacoes)

    def listar_todas_doacoes(self) -> List[Dict[str, Any]]:
        doacoes = self.collection.find()
        return list(doacoes)