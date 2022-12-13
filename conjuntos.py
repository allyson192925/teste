'''
Conjuntos 

- Conjuntos em qualquer linguagem de programação, estamos fazendo referências a teoria dos conjuntos
da Matemática.

- Aqui no Python, os conjuntos são chamaods de Sets.

Dito isto, da mesma forma que a matemática:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos são indexados;

Conjuntos são bons para se utilizar quando precisamos de armazenar elementos
mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar
com chaves, valores e itens duplicados.

Os conjuntos(sets) são referenciados em Python com chaves{}

Diferença entre os conjuntos (set) e mapas (Dicionários) em Python:
    - Um dicionário tem chaves/valor;
    - um conjunto tem apenas valor;

# Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 2, 3,})  # Repare que temos velores repetidos.

print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo 
# será ignorado sem gerar error e não fará parte do conunto.

# Forma 2 - Mais comum

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto

if 3 in s:
    print('tem o 3')
else:
    print('não tem o 3')

# Importante lembrar que, além de não termos valores duplicados, não temos ordem.



# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em sets

s = {1, 'b', True, 34, 22, 44}

print(s)
print(type(s))

# Podemos iterar em um set normalmente
for valor in s:
    print(s)

# Uso interessantes com sets

# Imagine que fizemos um formulário de cadastro de visitantes e uma feira ou museu e os vsitantes
# informam manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos 
# e ter repetição

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.

# O que voçê faria? Faria um loop na lista...?

# Podemos utizar o set para isso:

print(len(set(cidades)))

# Adicionando elementos em um conjunto
s = {1, 2, 3}

s.add(4)
s.add(4)  # Duplicidade não gera erro,. Simplismente é ignorado e não é adicionado.
print(s)

# Removendo elementos em um conjunto
s = {1, 2, 3}
print(s)

# Forma 1

s.remove(3)  # NÃO É INDICE, INFORMAMOS O VALOR A SER REMOVIDO.

print(s)

# OBS: Caso o valor não se encontrado será gerado o erro KeyError. Nenhum valor é retornado.

# Forma 2

s.discard(2)

print(s)

# OBS: Se o valor não for encontrado, nenhum erro é gerado

# Copiando um conjunto para outro...
s = {1, 2, 3}
print(s)

# Forma 1 - Deep copy

novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Forma 2 - Shallow copy
s = {1, 2, 3}
print(s)

novo = s

novo.add(4)

print(novo)
print(s)

# Métodos Matemáticos de Conjuntos

# Imagine que temos dois conjuntoa: um contendo estudantes do curso de Python e um 
# Contendo estudantes do curso de java.

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos estudam Python e também estudam Java.

# Pprecisamos gerar um conjunto com nomes de estudantes únicos.

# Forma 1 - Utilizando union

unicos1 = estudantes_python.union(estudantes_java)
#{'Pedro', 'Fernando', 'Ana', 'Julia', 'Guilherme', 'Patricia', 'Marcos', 'Elen', 'Gustavo'}
#unicos1 = estudantes_java.union(estudantes_python)
# {'Ana', 'Marcos', 'Gustavo', 'Fernando', 'Patriacia', 'Guilherme', 'Pedro', 'Elen', 'Julia'}
print(unicos1)

# Forma 2 - Utilizando o caractere pipe |
unicos2 = estudantes_python | estudantes_java

print(unicos2)

# Veja que alguns alunos estudam Python e também estudam Java.

# Gerar um conjunto de estudantes que estão em ambos os cursos.

# Forma 1 - utilizando intersection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando o & 

ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Métodos Matemáticos de Conjuntos

# Imagine que temos dois conjuntoa: um contendo estudantes do curso de Python e um 
# Contendo estudantes do curso de java.

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Gerar um conjunto de estudantes que não estão no outro curso
so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)


'''

# Soma*, Valor Máximo*, Valor Minímo, Tamanho
# * Se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))

