from db import _executar

class Produto:

    def __init__(self, nome, preco, id = None):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.status = 1 # Ativo = 1 / Inativo = 0

        #Se a tabela ñ existe, crie:
        query = "CREATE TABLE IF NOT EXISTS produtos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, preco REAL, status NUMERIC)"
        _executar(query)
    
    def save(self):
        query = f"INSERT INTO  produtos (nome, preco, status) VALUES ('{self.nome}', {float(self.preco)}, {self.status})"
        _executar(query)
    
    def updated(self):
        query = f"UPDATE produtos SET status={int(self.status)} WHERE id={int(self.id)}"
        _executar(query)

    def deleted(self):
        query = f"DELETE FROM produtos WHERE id={int(self.id)}"
        _executar(query)

    @staticmethod
    def get_produtos():
        query = "SELECT * FROM produtos"
        produtos = _executar(query)
        return produtos
    
    @staticmethod
    def get_produto(id):
        query = f"SELECT id, nome, preco FROM produtos WHERE id={int(id)}"
        produto = _executar(query)[0] # [0] pega o primeiro item da lista
        produto = Produto(id=produto[0], nome= produto[1], preco=produto[2])
        return produto
    
