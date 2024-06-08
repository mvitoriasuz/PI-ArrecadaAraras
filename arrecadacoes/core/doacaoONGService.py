from pymongo import MongoClient, ASCENDING
from pymongo.errors import DuplicateKeyError
from datetime import datetime

class DoacaoONGService:
    def __init__(self, db_name='arrecadacoes', uri='mongodb://localhost:27017/'):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db['clientes']
        self.collection.create_index([("email", ASCENDING)], unique=True)

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


class CadastroClienteService:
    def __init__(self, db_name='arrecadacoes', uri='mongodb://localhost:27017/'):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db['clientes']
        self.collection.create_index([("email", ASCENDING)], unique=True)

    def cadastrar_cliente(self, nome, cpf, email, senha, data_nascimento):
        try:
            documento = {
                "nome": nome,
                "cpf": cpf,
                "email": email,
                "senha": senha,
                "data_nascimento": data_nascimento,
                "data_cadastro": datetime.now()
            }
            result = self.collection.insert_one(documento)
            return {'success': True, 'inserted_id': str(result.inserted_id)}
        except DuplicateKeyError:
            return {'error': 'Este email já está cadastrado.'}