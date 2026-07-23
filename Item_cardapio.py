# Classe abstrata

from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    @abstractmethod
    def calcular_preco(self):
        pass

    @abstractmethod
    def tempo_preparo(self):
        pass
