from pymongo import MongoClient, ASCENDING
from pymongo.errors import DuplicateKeyError
from datetime import datetime
from typing import List, Dict, Any, Union

class DoacaoONGService:
    def __init__(self, db_name: str = 'arrecadacoes', uri: str = 'mongodb://localhost:27017/') -> None:
        self.client: MongoClient = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db['doacao_ong']
        self.collection.create_index([("email", ASCENDING)], unique=True)

    def listar_ongs(self) -> List[Dict[str, Any]]:
        ongs = self.collection.find({}, {"_id": 0, "senha": 0})
        return list(ongs)

    def registrar_doacao(self, ong_id: int, doacao: str) -> Dict[str, Union[str, bool]]:
        if not ong_id or not doacao:
            return {'error': 'O ID da ONG e a descrição da doação são obrigatórios.'}
        
        documento = {
            "ong_id": ong_id,
            "doacao": doacao,
            "data": datetime.now()
        }
        result = self.db['doacoes'].insert_one(documento)
        return {'inserted_id': str(result.inserted_id)}

    def listar_doacoes(self) -> List[Dict[str, Any]]:
        doacoes = self.db['doacoes'].find({}, {"_id": 0})
        return list(doacoes)

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
                "data_nasc": data_nasc
            }
            self.collection.insert_one(documento)
            return {"success": "Cliente cadastrado com sucesso."}
        except Exception as e:
            return {"error": str(e)}
        

    def listar_clientes(self) -> List[Dict[str, Any]]:
        clientes = self.collection.find({}, {"_id": 0, "senha": 0})
        return list(clientes)

    def inserir_clientes_exemplo(self) -> None:
        clientes_exemplo = [
            {"nome": "Fulano", "cpf": "12345678901", "email": "fulano@email.com", "senha": "senha123", "data_nascimento": "1990-01-01"},
            {"nome": "Ciclano", "cpf": "98765432109", "email": "ciclano@email.com", "senha": "senha456", "data_nascimento": "1985-05-15"}
        ]
        self.collection.insert_many(clientes_exemplo)
