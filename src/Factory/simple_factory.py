from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):

    @abstractmethod
    def falar(self):
        pass

class Cachorro(Animal):

    def falar(self):
        print("Au Au!")
        return "Au Au!"

class Gato(Animal):

    def falar(self):
        print("Miau!")
        return "Miau!"
    
# Fábrica
class AnimalFactory:

    def criar_animal(self, tipo):
        return eval(tipo)().falar() # eval é usado para instanciar a classe baseada no nome passado como string 

# Exemplo de uso
if __name__ == "__main__":
    factory = AnimalFactory()
    animal = input("Digite o tipo de animal (Cachorro ou Gato): ")
    factory.criar_animal(animal)


