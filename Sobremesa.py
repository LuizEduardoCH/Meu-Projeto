# Classe Sobremesa

from Item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco):
        super().__init__(nome, preco)

    def calcular_preco(self):
        return self.get_preco()

    def tempo_preparo(self):
        return 5