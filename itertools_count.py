from itertools import count

contador = count(start=1, step=2)

for valor in contador:
    print(round(valor, 2))

    if valor == 1000:
        break