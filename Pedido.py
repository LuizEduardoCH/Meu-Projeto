# Classe Pedido

from Prato import Prato
from Bebida import Bebida
from Sobremesa import Sobremesa

class Pedido:
    def __init__(self, maior_idade):
        self.itens = []
        self.maior_idade = maior_idade

    def adicionar_item(self, item):
        if isinstance(item, Bebida):
            if item.alcoolica and not self.maior_idade:
                print("Não é permitido vender bebida alcoólica para menores.")
                return False

        self.itens.append(item)
        return True

    def aplicar_brinde(self):
        qtd_pratos = 0

        for item in self.itens:
            if isinstance(item, Prato):
                qtd_pratos += 1

        if qtd_pratos >= 3:
            self.itens.append(Sobremesa("Pudim (Brinde)", 0))
            print("Sobremesa de brinde adicionada!")

    def total(self):
        soma = 0
        for item in self.itens:
            soma += item.calcular_preco()
        return soma

    def tempo_total(self):
        tempo = 0
        for item in self.itens:
            tempo += item.tempo_preparo()
        return tempo

    def mostrar_pedido(self):
        print("\nPEDIDO")
        for item in self.itens:
            print(f"- {item.get_nome()} - R$ {item.calcular_preco():.2f}")

        print(f"\nTotal: R$ {self.total():.2f}")
        print(f"Tempo de preparo: {self.tempo_total()} minutos")