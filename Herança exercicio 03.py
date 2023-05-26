class Forma:
    def __init__(self):
        self.area = 0
        self.perimetro = 0


class Retangulo(Forma):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def calculaArea(self):
        self.area = self.base * self.altura
        return self.area

    def calculaPerimetro(self):
        self.perimetro = 2 * (self.base + self.altura)
        return self.perimetro


class Triangulo(Forma):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def calculaArea(self):
        self.area = (self.base * self.altura) / 2
        return self.area

    def calculaPerimetro(self):
        self.perimetro = self.base + 2 * ((self.altura ** 2 + self.base ** 2) ** 0.5)
        return self.perimetro



retangulo = Retangulo(4, 6)
area_retangulo = retangulo.calculaArea()
perimetro_retangulo = retangulo.calculaPerimetro()

triangulo = Triangulo(5, 3)
area_triangulo = triangulo.calculaArea()
perimetro_triangulo = triangulo.calculaPerimetro()

print(f"Área do retângulo: {area_retangulo}")
print(f"Perímetro do retângulo: {perimetro_retangulo}")

print(f"Área do triângulo: {area_triangulo}")
print(f"Perímetro do triângulo: {perimetro_triangulo}")
