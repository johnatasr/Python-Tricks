from itertools import groupby

alunos = [{}, {}, {}]

ordena = lambda item:item['nota']
alunos.sort(ordena)
alunos_agrupado = groupby(alunos, ordena)

for agruapamento, valor in alunos_agrupado:
    ...