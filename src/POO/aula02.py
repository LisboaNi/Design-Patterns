from datetime import datetime

class Pessoa:

    def __init__(self, nome) -> None:
        self.nome = nome
        self.cadastro = datetime.now()
    
    def __str__(self): # Apresentar Objeto com Print
        return self.nome
    
    def __repr__(self): # Apresentar Objeto sem Print
        return self.nome

class Carro:

    def __init__(self, modelo: bool = False) -> None:
        self.modelo = modelo
        self.velocidade = 0
        self.motorista = None
    
    def __str__(self) -> str:
        if self.motorista:
            return f"{self.modelo} - {self.motorista.nome}"
        return "Sem motorista"
    
    def dirigir(self, motorista: Pessoa) -> None:
        self.motorista = motorista
        self.acelerar(1)
    
    def acelerar(self, velocidade: int) -> None:
        self.velocidade += velocidade

    def parar(self) -> None:
        self.velocidade = 0
