from abc import ABCMeta, abstractmethod

#Factory 
#Liskov Substituion 

class Produto(metaclass=ABCMeta):

    @abstractmethod
    def produto(self):
        pass

class Pizza(Produto):

    def produto(self):
        print('Pizza')
        return super().produto()

class Hamburguer(Produto):

    def produto(self):
        print('Hamburguer')
        return super().produto()

class Refrigerante(Produto):

    def produto(self):
        print('Refrigerante')
        return super().produto()
    
class ProdutoFactory:

    def solicitar(self, tipo):
        return eval(tipo)().produto()
    
if __name__ == '__main__':
    factory = ProdutoFactory()
    solicitar = input('Escolha: Pizza, Hamburguer ou Refrigerante:')
    factory.solicitar(solicitar)

#Singleton