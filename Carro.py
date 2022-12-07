class Carro:
    def __init__(self, nome, modelo, peso, cor):
        self.nome = nome
        self.modelo = modelo
        self.peso = peso
        self.cor = cor
    def ligar(self):
        print("Ligar")
    def desligar(self):
        print("Desligar")
    def mostrar_informacoes(self):
        print(f"a marca é {self.nome}, o modelo é {self.modelo}, o peso é {self.peso}, a cor é {self.cor}")

carro1 = Carro("Fiat", 500, "850kg", "branco")
carro1.ligar()
carro1.desligar()
carro1.mostrar_informacoes()


carro2 = Carro("Volkswagen", 500, "900kg", "azul")
carro2.ligar()
carro2.desligar()
carro2.mostrar_informacoes()
