from pymongo import MongoClient

class DatabaseService:
    def __init__(self, db_name, connection_string=None):
        """
        Inicializa a conexão com o MongoDB.

        :param db_name: Nome do banco de dados ao qual você deseja se conectar.
        :param connection_string: String de conexão opcional para especificar o host, porta e autenticação.
                                 Se não fornecido, tentará conectar-se ao MongoDB local.
        """
        if connection_string:
            self.client = MongoClient(connection_string)
        else:
            self.client = MongoClient('mongodb://localhost:27017/')
        
        self.db = self.client[db_name]

    def insert_document(self, collection_name, document):
        """
        Insere um documento em uma coleção especificada.

        :param collection_name: Nome da coleção onde o documento será inserido.
        :param document: Documento a ser inserido.
        """
        self.db[collection_name].insert_one(document)

    def find_documents(self, collection_name, query):
        """
        Encontra documentos em uma coleção especificada com base em uma consulta.

        :param collection_name: Nome da coleção onde a busca será realizada.
        :param query: Consulta a ser usada para encontrar os documentos.
        :return: Um cursor para iterar sobre os documentos encontrados.
        """
        return self.db[collection_name].find(query)

    # Você pode adicionar mais métodos conforme necessário para outras operações CRUD (Create, Read, Update, Delete).
