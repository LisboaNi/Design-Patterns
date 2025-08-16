class Ator:

    def __init__(self):
        self.ocupado = False
    
    def indisponivel(self):
        self.ocupado = True
        print(f'{type(self).__name__} está ocupado.')
    
    def disponivel(self):
        self.ocupado = False
        print(f'{type(self).__name__} está disponivel.')

    def disponibilidade(self):
        return self.ocupado

# Proxy
class Agente: 

    def trabalhar(self):
        ator = Ator()
        if ator.disponibilidade():
            ator.indisponivel()
        else:
            ator.disponivel()

# Cliente
if __name__ == '__main__':
    agente = Agente()
    agente.trabalhar()
