from abc import ABCMeta, abstractmethod

# Seções do Perfil
class Secao(metaclass=ABCMeta):

    @abstractmethod
    def __repr__(self):
        pass

class SecaoPessoal(Secao):

    def __repr__(self):
        return "Seção Pessoal"

class SecaoAlbum(Secao):

    def __repr__(self):
        return "Seção Album"
    
class SecaoProjetos(Secao):

    def __repr__(self):
        return "Seção Projetos"
    
class SecaoPublicacao(Secao):

    def __repr__(self):
        return "Seção Publicação"

# Fabrica de Perfis  
class Perfil(metaclass=ABCMeta):

    def __init__(self):
        self.secoes = []
        self.criar_perfil()
    
    @abstractmethod
    def criar_perfil(self):
        pass

    def get_secoes(self):
        return self.secoes
    
    def add_secao(self, secao):
        self.secoes.append(secao)

# Perfis Concretos
class Linkedin(Perfil):

    def criar_perfil(self):
        self.add_secao(SecaoPessoal())
        self.add_secao(SecaoProjetos())
        self.add_secao(SecaoPublicacao())

class Facebook(Perfil):

    def criar_perfil(self):
        self.add_secao(SecaoPessoal())
        self.add_secao(SecaoAlbum())

if __name__ == "__main__":
    rede_social = input("Digite a rede social (Linkedin ou Facebook): ")

    perfil = eval(rede_social)()  # eval é usado para instanciar a classe baseada no nome passado como string
    print(f"Perfil criado: {type(perfil).__name__}")
    print(f"Seções disponíveis: {perfil.get_secoes()}")