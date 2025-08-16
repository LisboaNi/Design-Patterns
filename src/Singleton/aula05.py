class Singleton(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'): # Verifica se existe o atributo instance
            cls.instance = super(Singleton, cls).__new__(cls) # Cria o objeto
            print(f"Criando o objeto {cls.instance}")
        return cls.instance # Retorna a instância criada anteriormente

s1 = Singleton()
print(f"Instancia {id(s1)}")

s2 = Singleton()
print(f"Instancia {id(s2)}")

# Mesmo que s1 e s2 sejam variáveis diferentes, ambas apontam para o mesmo objeto na memória
# Garantindo que apenas uma instância da classe Singleton seja criada