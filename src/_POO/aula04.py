from abc import ABC, abstractmethod
from uuid import uuid4

class Pessoa(ABC):
    def __init__(self, nome: str) -> None:
        self.nome = nome
    
    @abstractmethod
    def dinheiro(self) -> None:
        pass

class Aluno(Pessoa):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)
        self.__matricula = str(uuid4()).split('-')[0].upper()
    
    def dinheiro(self) -> None:
        print(f"{self.nome} tem dinheiro para pagar a mensalidade")

aluno1 = Aluno('Felicity')
print(aluno1.__dict__)