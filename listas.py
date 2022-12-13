"""
Listas 
Listas em Python funciona como vetores/matrizas (arrays) em outras linguagens, com a diferença 
de serem DINÂMICO e também de podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo:
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array
    será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.
    
Já em Python: 

- Dinâmico: Não possui tamanho fixo. Ou seja, podemos criar a lista e simplismente elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são representados por colchetes: []
"""
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'u', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

# Podemos facilmente checar se determinado valor esta na lista
num = 7
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o {num}')

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrêcias de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em listas

"""
Para adicionar elementos em listas, utilizamos a função append
"""

print(lista1)
lista1.append(42)
print(lista1)

#OBS: com append, nós só conseguimos adicionar 1 elemento por vez
#lista1.append(12, 35, 95) # erro 

lista1.append([8, 3, 1])
print(lista1)

if 22, 27, 27 in lista1:
    print('Encotrei a lista')
else:
    print('não encontrei a lista')