class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"O {self.nome} foi comer...")


class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def emitir_som(self):
        print(f"O {self.nome} está miando...")


class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def emitir_som(self):
        print(f"O {self.nome} está latindo...")


class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def mugir(self):
        print(f"A {self.nome} está muuuu...")


gato = Gato("Bola", "preto")
gato.comer()
gato.emitir_som()

cachorro = Cachorro("Rex", "marrom")
cachorro.comer()
cachorro.emitir_som()

vaca = Vaca("Mimosa", "branco e preto")
vaca.comer()
vaca.mugir()
