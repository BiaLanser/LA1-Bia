soma = 0

for i in range (5):
    valor = int(input("Digite um valor: "))

    soma += valor

media = soma / 5

print(f"A soma dos valores é {soma} \n e a média é {media:.2f}")