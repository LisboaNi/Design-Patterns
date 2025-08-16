import sqlite3

class Singleton(type):

    __instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instance[cls]
    
class Database(metaclass=Singleton):

    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect('example.db')
            self.cursor = self.connection.cursor() # Inserir, Atualizar, Deletar, Consultar
        return self.cursor

db1 = Database().connect()

db2 = Database().connect()