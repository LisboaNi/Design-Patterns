class Lanzy:
    __instance = None

    def __init__(self):
        if not Lanzy.__instance:
            print('Primeira instância')
        else:
            print(f'Instância já criada: {id(self.get_instance())}')
    
    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Lanzy()
        return cls.__instance
    
a = Lanzy() # Inicializa a primeira instância

print(f'Objeto: {id(Lanzy.get_instance())}')

b = Lanzy() # Retorna a instância já criada