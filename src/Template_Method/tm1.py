from abc import ABCMeta, abstractmethod

class Compilador(metaclass=ABCMeta):

    @abstractmethod
    def coletar(self):
        pass

    @abstractmethod
    def compilar(self):
        pass

    @abstractmethod
    def executar(self):
        pass

    def compilar_executar(self):
        self.coletar()
        self.compilar()
        self.executar()

class IOS(Compilador):
    
    def coletar(self):
        print('Coletando...Swift')
    
    def compilar(self):
        print('Compilando...LLVM')

    def executar(self):
        print('Executando...')

class Android(Compilador):
    
    def coletar(self):
        print('Coletando...Kotlin')
    
    def compilar(self):
        print('Compilando...JVM')

    def executar(self):
        print('Executando...')

ios = IOS()
ios.compilar_executar()

android = Android()
android.compilar_executar()