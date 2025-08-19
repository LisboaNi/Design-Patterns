from abc import ABCMeta, abstractmethod

class Abstrata(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def op1(self):
        pass

    @abstractmethod
    def op2(self):
        pass

    def templade(self):
        print('Op1 após a Op2')
        self.op2()
        self.op1()

class Concreta(Abstrata):

    def op1(self):
        print('OP1')
    
    def op2(self):
        print('OP2')

class Cliente:

    def main(self):
        self.concreta = Concreta()
        self.concreta.templade()

cliente = Cliente()
cliente.main()