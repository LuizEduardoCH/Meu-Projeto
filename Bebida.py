# Classe Bebida
from Item_cardapio import ItemCardapio


class Bebida(ItemCardapio ):
    def __init__(self, nome, preco, alcoolica):
        super().__init__(nome, preco)
        self.alcoolica = alcoolica

    def calcular_preco(self):
        return self.get_preco()

    def tempo_preparo(self):
        return 2