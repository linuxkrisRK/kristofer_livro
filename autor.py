"""
Kristofer R.K

"""


class Autor:
    contador = 0

    def __init__(self):
        self.__id = Autor.contador + 1
        self.nome = None
        Autor.contador += 1

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, i):
        self.__id = i

    def cadastrar_autor(self, n):
        self.nome = n

    def mostrar_autor(self):
        return f'ID do Autor: {self.id}\n' \
               f'Nome do Autor: {self.nome}'
