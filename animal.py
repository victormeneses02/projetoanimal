from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, nome, idade, peso):
        self.__nome=nome
        self.__idade=idade
        self.__peso=peso
    
    # Métodos get
    def getNome(self):
        return self.__nome
    def getIdade(self):
        return self.__idade
    def getPeso(self):
        return self.__peso
    
    # Métodos set
    def setNome(self, nome):
        self.__nome=nome
    def setIdade(self, idade):
        self.__idade=idade
    def setPeso(self, peso):
        self.__peso=peso
    
    @abstractmethod
    def mostrar(self):
        pass
    