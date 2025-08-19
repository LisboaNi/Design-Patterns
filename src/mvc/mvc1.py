class Modelo:

    def __init__(self):
        self.produtos = {
            'ps5': 
                {
                    'id': 1, 
                    'name': 'Playstation 5',
                    'preco': 1244
                },
            'xbox': 
                {
                    'id': 2, 
                    'name': 'Xbox 360',
                    'preco': 900
                },
            'wii': 
                {
                    'id': 3, 
                    'name': 'Nintendo Wii',
                    'preco': 1567
                }
        }

class Controlador:

    def __init__(self):
        self.modelo = Modelo()

    def listar(self):
        produtos = self.modelo.produtos.keys()

        print('---------------Produtos----------------')
        for produto in produtos:
            print(f"ID {self.modelo.produtos[produto]['id']}")
            print(f"Nome {self.modelo.produtos[produto]['name']}")
            print(f"Preço {self.modelo.produtos[produto]['preco']}\n")

class Visao:

    def __init__(self):
        self.controlador = Controlador()

    def produtos(self):
        self.controlador.listar()

if __name__ == '__main__':
    visao = Visao()
    visao.produtos()