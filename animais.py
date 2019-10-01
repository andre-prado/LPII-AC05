from mamifero import Mamifero
from reptil import Reptil

# cavalo, cachorro, gato / Cobra Jacare


class Cachorro(Mamifero):
    def __init__(self, nome, cor_pelo, idade, tipo_pata, raca):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.nome = nome
        self.cor_pelo = cor_pelo
        self.idade = idade
        self.tipo_pata = tipo_pata
        self.raca = raca

    def latir(self):
        return '{} latindo'.format(self.nome)

    def rosnar(self):
        return '{} rosnando'.format(self.nome)


class Gato(Mamifero):
    def __init__(self, nome, cor_pelo, idade, tipo_pata):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.nome = nome
        self.cor_pelo = cor_pelo
        self.idade = idade
        self.tipo_pata = tipo_pata
        self.vida = 7

    def miar(self):
        return '{} miando'.format(self.nome)

    def morrer(self):
        if self.vida == 0:
            return '{} morreu'.format(self.nome)
        else:
            self.vida -= 1
            return '{} tem {} vida(s) sobrando'.format(self.nome, self.vida)


class Cavalo(Mamifero):
    def __init__(self, nome, cor_pelo, idade, tipo_pata, cor_crina):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.nome = nome
        self.cor_pelo = cor_pelo
        self.idade = idade
        self.tipo_pata = tipo_pata
        self.cor_crina = cor_crina

    def galopar(self):
        return '{} galopando'.format(self.nome)

    def relinchar(self):
        return '{} relinchando'.format(self.nome)
