pares = []

for i in range(10):
    valor = int(input(f"Digite o {i + 1}º numero: "))

    if valor % 2 == 0:
        pares.append(valor)

print(f"Foram digitados: {len(pares)} valores pares")