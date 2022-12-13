"""
Loop for Loop -> Estrutura de repetição.
For -> Uma dessas estruturas

C ou Java

for (int i = 0; i < 10; i++){
    //execução do loop
}

Python
for item in interavel:
    //execução do loop
    
Utilizamos loops para iterar sobre sequências ou sobre valores iteravéis.

Exemplos de iteráveis:
- String
    nome = 'Geek University'
-Lista
    lista = [1, 3, 5, 7, 9]
-Range
    numeros = range(1, 10)
    
#exemplo de for 1 (iterando em uma string)
for letra in nome:
    print(letra)


# Exemplo de for 2 (iterando sobre uma lista)
for numero in lista:
    print(numero)
    
# Exemplo de for 3 (iterando sobre um range)
for numero in range(1, 10):
    print(numero)
 
 for i, v in enumerate(nome):
    print(nome[i])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)
### OBS:### Quando não precisamos de um valor, podemos descartá-lo utilizando um underline (_)

for valor in enumerate(nome):
    print(valor[0])
      
"""

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

