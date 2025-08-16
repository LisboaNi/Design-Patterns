#Metaclass Example

class University(type):

    def __call__(cls, *args, **kwargs):
        print(f'Argumentos...{args}')
        return type.__call__(cls, *args, **kwargs)

class Singleton(metaclass=University):

    def __init__(self, name):
        self.name = name

obj = Singleton('Universidade Federal de Goiás')

print(obj)