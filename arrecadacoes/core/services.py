from pymongo import MongoClient
from datetime import datetime
from typing import List, Dict, Any, Union

class CadastroClienteService:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['arrecadacoes']
        self.collection = self.db['doacao_ong']

    def cadastrar_cliente(self, nome: str, cpf: str, email: str, senha: str, data_nasc: str) -> dict:
        try:
            documento = {
                "nome": nome,
                "cpf": cpf,
                "email": email,
                "senha": senha,
                "data_nasc": data_nasc,
                "ong_id": None,
                "descricao_doacao": None,
                "data_doacao": None
            }
            self.collection.insert_one(documento)
            return {"success": "Cliente cadastrado com sucesso."}
        except Exception as e:
            return {"error": str(e)}
        
    def fazer_doacao(self, cliente_id: str, ong_id: str, descricao_doacao: str) -> dict:
        try:
            # Atualiza o documento do cliente com as informações da doação
            self.collection.update_one(
                {"_id": cliente_id},
                {"$set": {
                    "ong_id": ong_id,
                    "descricao_doacao": descricao_doacao,
                    "data_doacao": datetime.now()
                }}
            )
            return {"success": "Doação registrada com sucesso."}
        except Exception as e:
            return {"error": str(e)}

    def listar_clientes(self) -> List[Dict[str, Any]]:
        clientes = self.collection.find({}, {"_id": 0, "senha": 0})
        return list(clientes)