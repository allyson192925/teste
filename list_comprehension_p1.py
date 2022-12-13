"""
List Cromprehension

- Utilizando Lis Comprehension nós podemos gerar novas listas com dados processados a partir de outro 
iterável.

# Sintaxe da List Comprehension

(dado for dado in iterável)


"""
# Exemplos

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)

"""
Para entender melhor o que está acontecendo devemos dividir a EXPRESSÃO em duas partes

- A primeira parte; for numero in numeros
-- A segunda parte: numero * 10

"""

res = [numero / 2 for numero in numeros]
print(res)

def funcao(valor):
    return valor * valor

res = [funcao(numero) for numero in numeros]
print(res)


