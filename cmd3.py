from abc import ABCMeta, abstractmethod

#Comando
class Ordem(metaclass=ABCMeta):

    @abstractmethod
    def executar(self):
        pass

#ComandoConcreto
class OrdemCompra(Ordem):

    def __init__(self, acao):
        self.acao = acao 

    def executar(self):
        self.acao.comprar()

class OrdemVenda(Ordem):

    def __init__(self, acao):
        self.acao = acao 
    
    def executar(self):
        self.acao.vender()

#Receiver
class Acao:

    def comprar(self):
        print('Compra')

    def vender(self):
        print('Vender')

#Invoker
class Agente:

    def __init__(self):
        self.__fila_ordens = []
    
    def add(self, ordem):
        self.__fila_ordens.append(ordem)
        ordem.executar()

# Cliente
if __name__ == '__main__':

    acao = Acao()
    ordem_compra = OrdemCompra(acao)
    ordem_venda = OrdemVenda(acao)

    agente = Agente()
    agente.add(ordem_compra)
    agente.add(ordem_venda)