from pymongo import MongoClient, ASCENDING
from pymongo.errors import DuplicateKeyError
from datetime import datetime

class DoacaoONGService:
    def __init__(self, db_name='arrecadacoes', uri='mongodb://localhost:27017/'):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db['doacao_ong']
        # Verificando duplicidade no email
        self.collection.create_index([("email", ASCENDING)], unique=True)

    def registrar_ong(self, nome, email, cpf, senha):
        return {'error': 'O cadastro de ONGs deve ser feito em uma tela separada.'}

    def listar_ongs(self):
        ongs = self.collection.find({}, {"_id": 0, "senha": 0})
        return list(ongs)

    def registrar_doacao(self, ong_id, doacao):
        if not ong_id or not doacao:
            return {'error': 'O ID da ONG e a descrição da doação são obrigatórios.'}
        
        documento = {
            "ong_id": ong_id,
            "doacao": doacao,
            "data": datetime.now()
        }
        result = self.db['doacoes'].insert_one(documento)
        return {'inserted_id': str(result.inserted_id)}

    def listar_doacoes(self):
        doacoes = self.db['doacoes'].find({}, {"_id": 0})
        return list(doacoes)
