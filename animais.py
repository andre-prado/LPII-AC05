from mamifero import Mamifero
from reptil import Reptil

# cavalo, cachorro, gato / Cobra Jacare


class Cachorro(Mamifero):
    def __init__(self, nome, cor_pelo, idade, tipo_pata):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.nome = nome
        self.cor_pelo = cor_pelo
        self.idade = idade
        self.tipo_pata = tipo_pata
