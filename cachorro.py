from animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, idade, peso, cPorte):
        super().__init__(nome, idade, peso)
        self.__cPorte=cPorte
    
    # Métodos set
    def setCPorte(self, porte):
        self.__cPorte=porte
    
    # Métodos get
    def getPorte(self):
        return self.__cPorte
    
    # Métodos de mostrar as Caraterídticas do cachorro
    def mostrar(self):
        return(f"O nome do cão: {self.getNome()}, Idade: {self.getIdade()}, Peso: {self.getPeso()} e Porte: {self.getPorte()}")
    
# Teste para verificar
#c = Cachorro("Thor", "8 anos", "12 kg", "Rottweiler")
#print(c.mostrar())