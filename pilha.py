"""
Kristofer R.K
Estrutura de dados

PILHA!

@Lifo = Last In First Out = O último a entrar é o primeiro a sair

"""
from node import Node


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    # Inserir um elemento na pilha.
    def add(self, elem):
        node = Node(elem)
        # Novo topo da pilha
        node.next = self.top
        self.top = node
        self._size = self._size + 1
        print('Elemento inserido!')

    # Remover o elemento do topo da pilha.
    def remove(self):
        # Verificar se a pilha possui itens.
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            # Diminuir o tamanho (len)
            self._size = self._size - 1
            print('Livro abaixo removido')
            r = node.data
            return r.mostrar_livros()
        raise IndexError("Erro, a pilha está vazia!")

    # Retorna o topo da pilha sem remover
    def peek(self):
        # Verificar se a pilha possui itens.
        if self._size > 0:
            print('Topo da pilha!')
            x = self.top.data
            return x.mostrar_livros()
        raise IndexError("Erro, a pilha está vazia!")

    # Retornar o tamanho da pilha
    def __len__(self):
        return self._size

    def imprimir(self):
        pointer = self.top
        if self._size <= 0:
            return f'Pilha vazia \n======================================================= \n'
        else:
            while pointer:
                x = pointer.data
                print(f'{x.mostrar_livros()}\n')
                pointer = pointer.next
