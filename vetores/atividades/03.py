numeros = []
maior = 0
menor = 0

for i in range(5):
    valor = int(input(f"Digite seu {i + 1}º número: "))
    numeros.append(valor)
    if i == 0:
        maior = valor
        menor = valor
    if valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor

print (f"""
O maior número é: {maior}
O menor número é: {menor}
""")