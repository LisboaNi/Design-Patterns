from abc import ABCMeta, abstractmethod

class Pacote(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def ida(self):
        pass

    @abstractmethod
    def dia1(self):
        pass

    @abstractmethod
    def dia2(self):
        pass

    @abstractmethod
    def dia3(self):
        pass

    @abstractmethod
    def retorno(self):
        pass

    def viagem(self):
        self.ida()
        self.dia1()
        self.dia2()
        self.dia3()
        self.retorno()

class Veneza(Pacote):

    def ida(self):
        print('Avião')

    def dia1(self):
        print('Visita à Basilica')

    def dia2(self):
        print('Visita ao Palácio')
    
    def dia3(self):
        print('Aproveitar a comida na Ponte')
    
    def retorno(self):
        print('Avião')

class Malvinas(Pacote):

    def ida(self):
        print('Ônibus')

    def dia1(self):
        print('Visita à vida marinha')

    def dia2(self):
        print('Praticar esportes')
    
    def dia3(self):
        print('Relaxar na praia')
    
    def retorno(self):
        print('Ônibus')

class Travel:

    def preparar(self):
        opcao = input('Veneza ou Malvinas:')

        if opcao == 'Veneza':
            self.pacote = Veneza()
            self.pacote.viagem()
        elif opcao == 'Malvinas':
            self.pacote = Malvinas()
            self.pacote.viagem()
        else:
            print('Invalido')

agencia = Travel()
agencia.preparar()