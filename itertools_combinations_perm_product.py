from itertools import (
    combinations,
    permutations,
    product
)

pessoas = ['Joao', 'Pedro', 'Marcos', 'Paulo']
# Sem repeticao

for grupo in combinations(pessoas, 2):
    print(grupo)

# COm repeticao de ordem
for grupo in permutations(pessoas, 2):
    print(grupo)

#geram grupos
for grupo in product(pessoas, 4):
    print(grupo)