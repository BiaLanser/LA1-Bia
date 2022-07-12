maior_valor = 0
menor_valor = 0

valor = float(input("Digite um valor: "))
maior_valor = valor
menor_valor = valor

for i in range(4):
    valor = float(input("Digite um valor: "))
     
    if valor > maior_valor:
        maior_valor = valor
    elif valor < menor_valor:
        menor_valor = valor
    else:
        continue

print(f"Maior valor: {maior_valor} \nMenor valor: {menor_valor}")
    