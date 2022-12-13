"""
Mapas => conhecido em Python como Diciónarios

Iterar sobre Diciónarios
for chave in receita:
    print(receita[chave])
    
for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')

print(receita.keys())

for chave in receita:
    print(receita[chave])
    
#Acessando os valores 
print(receita.values())

for valor in receita.values():
        print(valor)

"""
receita = {'jan': 100, 'fev': 250, 'mar': 400}

print(receita)
print(receita.items())

for chave, valor in receita.items():
    print(f'Chave={chave} e valor={valor}')
