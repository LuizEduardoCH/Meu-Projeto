# Classe Prato

from Item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, complexidade):
        super().__init__(nome, preco)
        self.complexidade = complexidade

    def calcular_preco(self):
        return self.get_preco()

    def tempo_preparo(self):
        if self.complexidade == "simples":
            return 15
        elif self.complexidade == "media":
            return 25
        else:
            return 40