"""
Tuplas (tuple)

Tuplas são bastante parecidas com Listas.

Existem basicamente duas diferenças basicas: 

1 - As tuplas são representadas por pasênteses ()

2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda. Toda 
operação em uma tupla gera uma nova tupla.


# CUIDADO 1: As tuplas são representadas por (),mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# CUIDADOS 2: Tuplas com 1 elemento

tupla3 = (4) # isso não é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (4, ) # Isso é uma tupla
print(tupla4)
print(type(tupla4))

tupla5 = 4,
print(tupla5)
print(type(tupla5))

#CONCLUSÃO: Podemos concluir que são definidos pela vírgula e não pelo uso do parênteses
(4) -> Não é tupla
(4,) -> É tupla 
4, -> É tupla

# Podemos gerar uma tupla dinâmica usando o range(inicio, fim, passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla

tupla = ('Geek University', 'Programação em Python: Essencial')

escola, curso = tupla

print(escola)
print(curso)

# OBS: Gera erro (ValueError) se colocarmos um número diferente de elementos para desempacotar.
# Métodos para adição e remoção de elementos nas tuplas são existem, dado o fato das tuplas serem imutáveis.

# Soma*, Valor Máximo*, Valor Minimo* e tamanho

# Se os valores forem todos inteiros ou reias

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 10)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas 

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2) # Tuplas são imutáveis

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2

print(tupla3)
print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2 # Tuplas são imutáveis, mas podemos sobrescrever seus valores
print(tupla1)

# Verificar se determinado elemento esta contido na tupla

tupla = (1, 2, 3)
print(3 in tupla)

# Interando sobre uma tupla

tupla = (1, 2, 3)

for n in tupla:
    print(n)
    
for indice, valor in enumerate(tupla):
    print(indice, valor)
    
# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(tupla.count('a'))

escola = tuple('Geek University')
print(escola)

print(escola.count('e'))

# Dicas na utilização de tuplas 

# Devemos utilizar tuplas SEMPRE que não precisarmos modifucar os dados contidos em uma coleção

# Exemplo 1

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# Slicing

# tupla[inicio:fim:passo]

print(meses[5:9○])

# O acesso a elementos de uma tupla também é semelhante a de uma lista

print(meses[8])

# Iterar com while 
i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1
    # Verificando em qual indice um elemento está na tupla
print(meses.index('Junho'))

# OBS: Caso o elemento não exista, será gerado ValueError

# Por que trabalhar com tuplas?

# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam seu código mais seguro*
# - Isso porque trabalhar com elementos imutaveis trás segurança para o código.    

# Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla # Na tupla não temos o problema de Shallow Copy

print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra

print(nova)
print(tupla)

"""


