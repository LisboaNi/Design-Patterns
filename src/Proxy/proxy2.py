from abc import ABCMeta, abstractmethod

# Interface
class Carteira(metaclass=ABCMeta):

    @abstractmethod
    def pagar(self):
        pass

# Objeto Real
class Banco(Carteira):

    def __init__(self):
        self.cartao = None
        self.conta = None
    
    def get_conta(self):
        self.conta = self.cartao

        return self.conta
    
    def saldo(self):
        print(f'Conta {self.get_conta()}')
        return True

    def set_cartao(self, cartao):
        self.cartao = cartao

    def pagar(self):
        if self.saldo():
            print('Pagar')
            return True
        else:
            print('Sem saldo')
            return False
        
# Proxy
class CartaoDebido(Carteira):

    def __init__(self):
        self.banco = Banco()
    
    def pagar(self):
        cartao = input("Proxy")
        self.banco.set_cartao(cartao)
        return self.banco.pagar()

# Cliente
class Cliente:

    def __init__(self):
        print('Compra')
        self.cartao_debito = CartaoDebido()
        self.comprei = None
    
    def pagamento(self):
        self.comprei = self.cartao_debito.pagar()

    def __del__(self):
        if self.comprei:
            print('comprei')
        else:
            print('Não comprei')

if __name__ == '__main__':
    cliente = Cliente()
    cliente.pagamento()