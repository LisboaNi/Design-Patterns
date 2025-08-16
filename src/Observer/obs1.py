class Observer:

    def __init__(self):
        self.__observadores = []
    
    def __repr__(self):
        return 'Obj'
    
    def registrar(self, observador):
        self.__observadores.append(observador)

    def notificar_todos(self, *args, **kwargs):
        for observador in self.__observadores:
            observador.notificar(self, *args, **kwargs)

class ObsA:

    def __init__(self, objeto):
        objeto.registrar(self)

    def notificar(self, objeto, *args):
        print(f'{type(self).__name__} recebeu uma {args[0]} de {objeto}')

class ObsB:

    def __init__(self, objeto):
        objeto.registrar(self)

    def notificar(self, objeto, *args):
        print(f'{type(self).__name__} recebeu uma {args[0]} de {objeto}')

obj = Observer()
obs_a = ObsA(obj)
obs_b = ObsB(obj)

obj.notificar_todos('notificação')

