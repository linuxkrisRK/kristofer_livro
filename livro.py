"""
Kristofer R.K

"""


class Livro:
    contador = 10

    def __init__(self):
        self.__id = Livro.contador + 1
        self.__titulo = None
        self.__autor = None
        Livro.contador += 1

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, i):
        self.__id = i

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, t):
        self.__titulo = t

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, a):
        self.__autor = a

    def cadastrar_livros(self, t, a):
        self.titulo = t
        self.autor = a

    def mostrar_livros(self):
        return f'ID: {self.id} \n' \
               f'Titulo: {self.titulo}\n' \
               f'Autor: {self.autor.mostrar_autor()}'

