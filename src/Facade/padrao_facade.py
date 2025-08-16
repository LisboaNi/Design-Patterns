#Facade
class GerenciamentoEventos:

    def __init__(self):
        print('Gerenciamento\n\n')
    
    def organizar(self):
        self.salao = SalaoFestas()
        self.salao.agendar()

        self.florista = Florista()
        self.florista.flores()

        self.comida = Restaurante()
        self.comida.preparar()

        self.musica = Banda()
        self.musica.palco()

# Subsistema 1
class SalaoFestas:

    def __init__(self):
        print('Agendando...')
    
    def _disponivel(self):
        print('Disponivel?')
        return True
    
    def agendar(self):
        if self._disponivel():
            print('Agendado\n')

# Subsistema 2
class Florista:

    def __init__(self):
        print('Flores?')

    def flores(self):
        print('Rosas\n')

# Subsistema 3
class Restaurante:

    def __init__(self):
        print('Comida?')
    
    def preparar(self):
        print('Brasileira\n')

# Subsistema 4
class Banda:

    def __init__(self):
        print("Musicas")
    
    def palco(self):
        print('Palco\n')

# Cliente
class Cliente:

    def __init__(self):
        print('Cliente')
    
    def contratar(self):
        print('Contratando...\n')

        ge = GerenciamentoEventos()
        ge.organizar()
    
    def __del__(self): # Dps é deletado da memória
        print('Simples / Finalizado Evento')

if __name__ == '__main__':
    Cliente = Cliente()
    Cliente.contratar()