from abc import ABCMeta

class Estado(metaclass=ABCMeta):
    nome = 'estado'
    permitido = []

    def mudar(self, estado):
        if estado.nome in self.permitido:
            print(f'Atual: {self} => mudado para um novo estado: {estado.nome}')
            self.__class__ = estado
        else:
            print(f'Atual: {self} => não é possivel mudar para: {estado.nome}')
    
    def __str__(self):
        return self.nome
    
class Ligar(Estado):
    nome = 'Ligar'
    permitido = ["Desligar", "Suspender", "Hibernar"]

class Desligar(Estado):
    nome = 'Desligar'
    permitido = ["Ligar"]

class Suspender(Estado):
    nome = 'Suspender'
    permitido = ["Ligar"]

class Hibernar(Estado):
    nome = 'Hibernar'
    permitido = ["Ligar"]

class Computador: 

    def __init__(self, modelo = 'Dell'):
        self.modelo = modelo
        self.estado = Desligar()

    def alterar(self, estado):
        self.estado.mudar(estado)

if __name__ == '__main__':
    comp = Computador()

    comp.alterar(Ligar)

    comp.alterar(Desligar)

    comp.alterar(Ligar)

    comp.alterar(Suspender)

    comp.alterar(Hibernar)

    comp.alterar(Ligar)

    comp.alterar(Desligar)