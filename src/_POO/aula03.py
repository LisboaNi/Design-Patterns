from typing import List, Tuple

class Curso:

    def __init__(self, nome: str = 'Curso', carga: int = 45) -> None:
        self.__nome = nome
        self.__carga = carga
    
Curso1: Curso = Curso('Python', 60)
Curso2: Curso = Curso('Java', 80)

# print(Curso1.__dict__)
# print(Curso2.__dict__)

# ---------------------------------------------------------

nome: str = 'Python'
tupla: Tuple = (1, 2, 3, 4, 5)
lista: List = [1, 2, 3]

# print(nome[:6], tupla[:3], lista[:4])

# ---------------------------------------------------------

class Pessoa:
    def __init__(self, nome: str) -> None:
        self.__nome = nome

    def andar(self) -> None:
        print(f"{self.__nome} está andando")

class Aluno(Pessoa):
    def __init__(self, nome: str, matricula: str) -> None:
        super().__init__(nome)
        self.__matricula = matricula

felicity = Aluno('Felicity', '12345')

# felicity.andar()

# ---------------------------------------------------------


def gerar_fibonacci(qtd: int) -> None:
    if qtd <=0:
        print("Quantidade inválida")
    else:
        print(f"Gerando Fibonacci com {qtd} números")
        contador: int = 0
        n1: int = 0
        n2: int = 1
        while contador < qtd:
            print(n1)
            proximo = n1 + n2
            n1 = n2
            n2 = proximo
            contador += 1

# gerar_fibonacci(10)

# ---------------------------------------------------------

class Motor:
    def ligar(self) -> None: 
        print("Motor ligado")

class Pneu:
    def encher(self) -> None:
        print("Pneu cheio")

class Carro:
    def __init__(self, modelo: str) -> None:
        self.modelo = modelo
        self.motor = Motor()
        self.pneu1 = Pneu()
        self.pneu2 = Pneu()
        self.pneu3 = Pneu()
        self.pneu4 = Pneu()

# fusca = Carro("Fusca")
# fusca.motor.ligar()
# fusca.pneu1.encher()