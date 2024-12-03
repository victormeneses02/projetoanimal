from animal import Animal

class Gato(Animal):
    def __init__(self, nome, idade, peso, nRaca):
        super().__init__(nome, idade, peso)
        self.__nRaca=nRaca
    
    # Métodos set
    def setNRaca(self, raca):
        self.__nRaca=raca
    
    # Métodos get
    def getNRaca(self):
        return self.__nRaca
    
    # Métodos de mostrar as Caraterídticas do gato
    def mostrar(self):
        return (f"O nome do gato: {self.getNome()}, Idade: {self.getIdade()}, Peso: {self.getPeso()} e Raça: {self.getNRaca()}")
    
# Teste para verificar
#g = Gato("Edwiges", "3 anos", "4 kg", "Sphynx")
#print(g.mostrar())