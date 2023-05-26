class Pessoa:
    def __init__(self, nome, peso, idade, comendo=False, falando=False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def apresentar(self):
        memoria = print(f'{self.nome}')
        return memoria

    def comer(self, comida):
        if not self.comendo and not self.falando:
            self.comendo = True
            memoria = print(f'Agora {self.nome} está comendo uma {comida}')
            return memoria
        elif self.falando:
            print('Não pode comer enquanto fala!')
        else:
            memoria = print(f'{self.nome} já está comendo.')
            return memoria

    def parar_de_comer(self):
        if self.comendo:
            self.comendo = False
            memoria = print(f'Agora {self.nome} não está mais comendo!')
            return memoria
        else:
            memoria = print(f'{self.nome} não está comendo!')
            return memoria

    def falar(self):
        if not self.comendo and not self.falando:
            print('falando pô')
            self.falando = True
        elif self.comendo:
            print('não pode falar comendo!')
        elif self.falando:
            print('já está falando!')

    def parar_de_falar(self):
        if self.falando:
            print('Parou de falar')
            self.falando = False
        else:
            print('não está falando!')


a = Pessoa("Ricardo", 61, 22)

print(a.apresentar())
print(vars(a))

a.comer("Manga")
a.comer("Uva")
a.falar()
a.parar_de_comer()
a.parar_de_comer()
a.falar()
a.falar()
a.comer("Uva")
a.parar_de_falar()
a.parar_de_falar()




