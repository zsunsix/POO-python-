class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def imprimeValor(self):
        print(f"Valor do ingresso: R${self.valor}")


class VIP(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)


    def imprimeValor(self, adicional):
        total = self.valor+self.valor*adicional/100




normal = Ingresso(50)
normal.imprimeValor()

vip = VIP(100)
vip.imprimeValor(10)

