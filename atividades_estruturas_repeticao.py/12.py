soma = 0
contador = 0

while True:
    valor = int(input("Digite um valor: "))

    if valor < 0:
        break

    soma += valor
    contador += 1

media = soma / contador
print(f"A média dos valores digitados é: {media:.2f}")