class Atleta():
    def __init__(self,nome=str(),peso=float()):
        self.aposentado = False
        self.nome=nome
        self.peso=peso
        self.aquecido = False

    def aposentar(self):
        self.aposentado = True
        print(f"O atleta {self.nome} se aposentou")

    def aquecer(self):
        if self.aposentado == True:
           print(f"O atleta {self.nome} está aposentado, não pode aquecer")
        else:
            if self.aquecido == True:
                print(f"O atleta {self.nome} ja está aquecido")
            else:
                self.aquecido = True
                print(f"O atleta {self.nome} está aquecido")

    def pararAquecer(self):
        if self.aquecido == False:
            print(f"O atleta {self.nome} não está aquecido")

        else:
            self.aquecido = False
            print(f"O atleta {self.nome} parou de aquecer")

class Corredor(Atleta):
    def __init__(self,nome=str(),peso=float()):
        super().__init__()
        self.correndo=False
        self.nome=nome
        self.peso=peso

    def correr(self):
        if self.aquecido == True:
            if self.aposentado==True:
                print(f"O atleta {self.nome} está aposentado, não pode correr")

            elif self.correndo == True:
                print(f"O atleta já está correndo")

            else:
                self.correndo = True
                print(f"O atleta está correndo")
        else:
            print("O atleta precisa aquecer")

    def pararCorrer(self):
        if self.correndo == False:
            print("O atleta não está correndo")

        else:
            self.correr=False
            print("O atleta parou de correr")

class Nadador(Atleta):
    def __init__(self,nome=str(),peso=float()):
        super().__init__()
        self.nadando=False
        self.nome=nome
        self.peso=peso

    def nadar(self):
        if self.aquecido == True:
            if self.aposentado == True:
                print(f"O atleta {self.nome} está aposentado, não pode nadar")

            elif self.nadando == True:
                print(f"O atleta já está nadando")

            else:
                self.nadando = True
                print(f"O atleta está nadando")
        else:
            print("O atleta precisa aquecer")

    def pararNadar(self):
        if self.nadando == False:
            print("O atleta não está nadando")

        else:
            self.nadando = False
            print("O atleta parou de nadar")

class Ciclista(Atleta):
    def __init__(self,nome=str(),peso=float()):
        super().__init__()
        self.pedalando=False
        self.nome=nome
        self.peso=peso

    def pedalar(self):
        if self.aquecido == True:
            if self.aposentado == True:
                print(f"O atleta {self.nome} está aposentado, não pode pedalar")

            elif self.pedalando == True:
                print(f"O atleta já está pedalando")

            else:
                self.pedalando = True
                print(f"O atleta está pedalando")
        else:
            print("O atleta precisa aquecer")

    def pararPedalar(self):
        if self.pedalando == False:
            print("O atleta não está pedalando")

        else:
            self.pedalando = False
            print("O atleta parou de pedalar")

class Triatleta(Ciclista,Corredor,Nadador):
    def __init__(self,nome=str(),peso=float()):
        super().__init__()
        self.nome=nome
        self.peso=peso
        self.correndo=False
        self.pedalando=False
        self.nadando=False

    def correr(self):
        if self.nadando == False and self.pedalando == False:

            if self.aquecido == True:
                if self.aposentado == True:
                    print(f"O atleta {self.nome} está aposentado, não pode correr")

                elif self.correndo == True:
                    print(f"O atleta já está correndo")

                else:
                    self.correndo = True
                    print(f"O atleta está correndo")
            else:
                print("O atleta precisa aquecer")

        else:
            print("O atleta já está fazendo um exercicio")

    def nadar(self):
        if self.correndo == False and self.pedalando == False:
            if self.aquecido == True:
                if self.aposentado == True:
                    print(f"O atleta {self.nome} está aposentado, não pode nadar")

                elif self.nadando == True:
                    print(f"O atleta já está nadando")

                else:
                    self.nadando = True
                    print(f"O atleta está nadando")
            else:
                print("O atleta precisa aquecer")

        else:
            print("O atleta já está fazendo um exercicio")

    def pedalar(self):
        if self.nadando == False and self.correndo == False:
            if self.aquecido == True:
                if self.aposentado == True:
                    print(f"O atleta {self.nome} está aposentado, não pode pedalar")

                elif self.pedalando == True:
                    print(f"O atleta já está pedalando")

                else:
                    self.pedalando = True
                    print(f"O atleta está pedalando")
            else:
                print("O atleta precisa aquecer")

        else:
            print("O atleta já está fazendo um exercicio")


Ricardo=Triatleta("Ricardo", 61)

Ricardo.pedalar()
Ricardo.aquecer()
Ricardo.nadar()
Ricardo.correr()
Ricardo.pararNadar()
Ricardo.correr()
Ricardo.pedalar()





