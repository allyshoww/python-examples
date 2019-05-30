#! /usr/bin/python3

lista = ['a', 'b', 'c', 'd']

# Insere um objeto no final da lista
lista.append('e')
print(lista)

# Insere um objeto no começo da lista
lista.insert(0, 'A')
print(lista)

# Remove o ultimo item da lista
lista.pop()
print(lista)

# Remove determinando item da lista
lista.remove('a')

# Remove determinado item da lista
lista.pop(0)
print(lista)

# Ordena uma lista
lista.sort()

# Escreve a lista de trás para frente
lista.reverse()

# Busca um item dentro da lista - modo interativo funciona
lista.index('a')

# Conta quandos elementos estão dentro de uma lista
len(lista)
