from random import randint


lancamentos = []
quantidade = [0, 0, 0, 0, 0, 0]

for i in range (100):
    valor_lancado = randint(1, 6)

    if valor_lancado == 1:
        quantidade[0] += 1
    elif valor_lancado == 2:
        quantidade[1] += 1
    elif valor_lancado == 3:
        quantidade[2] += 1
    elif valor_lancado == 4:
        quantidade[3] += 1
    elif valor_lancado == 5:
        quantidade[4] += 1
    else:
        quantidade[5] += 1
    
    lancamentos.append(valor_lancado)

print(lancamentos)
for i, quantidade in enumerate(quantidade):
    print(f"Face {i + 1}: {quantidade}")