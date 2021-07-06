"""
Kristofer R.K

"""

from autor import Autor
from livro import Livro
from pilha import Stack

# ======================================================================================================================
# Testes

# Autor
a1 = Autor()
a1.cadastrar_autor('Kristofer')
# ======================================================================================================================

# Livro
l1 = Livro()
l1.cadastrar_livros('Livro do Kristofer', a1)
print(l1.mostrar_livros())
print('\n')

l2 = Livro()
l2.cadastrar_livros('Livro de Python', a1)
print(l2.mostrar_livros())
print('\n')

l3 = Livro()
l3.cadastrar_livros('JavaBase', a1)
print(l3.mostrar_livros())
print('\n')

# ======================================================================================================================

# Pilha
pilha = Stack()
pilha.add(l1)
pilha.add(l2)
pilha.add(l3)
print('\n')

print('Imprimindo pilha de livros\n')
pilha.imprimir()
print('\n')

print('Tamanho da pilha')
print(len(pilha))
print('\n')

print('--------------------------------------------------------------------')
print('Mostrar topo da pilha\n')
print(pilha.peek())
print('\n')

print('Elemento do topo removido!\n')
print(pilha.remove())
print('\n')

print('Imprimindo pilha de livros\n')
pilha.imprimir()
print('\n')

print('Tamanho da pilha')
print(len(pilha))



