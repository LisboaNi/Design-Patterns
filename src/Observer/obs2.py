from abc import ABCMeta, abstractmethod

# Assunto / Topico
class AgenciaNoticias:

    def __init__(self):
        self.__inscritos = []
        self.__noticia = None

    def inscrever (self, inscrito):
        self.__inscritos.append(inscrito)
    
    def desinscrever (self, inscrito = None):
        if not inscrito:
            return self.__inscritos.pop()
        else:
            return self.__inscritos.remove(inscrito)
    
    def notificar_todos(self):
        for insc in self.__inscritos:
            insc.notificar()
    
    def add_notifica(self, noticia):
        self.__noticia = noticia
    
    def mostrar(self):
        return f'Urgente {self.__noticia}'
    
    def inscritos(self):
        return [type(valor).__name__ for valor in self.__inscritos]
    
# Interface
class TipoInscricao(metaclass=ABCMeta):

    @abstractmethod
    def notificar(self):
        pass

# Observador A
class inscritosSMS(TipoInscricao):

    def __init__(self, noticia):
        self.noticia = noticia
        self.noticia.inscrever(self)
    
    def notificar(self):
        print (f'{type(self).__name__}{self.noticia.mostrar()}')

# Observador B
class inscritosEmail(TipoInscricao):

    def __init__(self, noticia):
        self.noticia = noticia
        self.noticia.inscrever(self)
    
    def notificar(self):
        print (f'{type(self).__name__}{self.noticia.mostrar()}')

# Observador N
class inscritosMeio(TipoInscricao):

    def __init__(self, noticia):
        self.noticia = noticia
        self.noticia.inscrever(self)
    
    def notificar(self):
        print (f'{type(self).__name__}{self.noticia.mostrar()}')

# Cliente
if __name__ == '__main__':
    noticia = AgenciaNoticias()

    inscritosSMS(noticia)
    inscritosEmail(noticia)
    inscritosMeio(noticia)

    print(f'Incritos: {noticia.inscritos()}')

    noticia.add_notifica('Novo')
    noticia.notificar_todos()

    print(f'Descadastrado: {type(noticia.desinscrever()).__name__}')
    print(f'Incritos: {noticia.inscritos()}')

    noticia.add_notifica('Design')
    noticia.notificar_todos()