num = []
# 1ª vez -> i = 0; indice de num é 0 [1]
# 2ª vez -> i = 1; indice de num é 1 [1, 2]
# 3ª vez -> i = 2; indice de num é 2 [1, 2, 3]
maior = 0
posicao = 0
for i in range(4):
    valor = int(input(f"Digite seu {i + 1}º número: "))
    num.append(valor)

    if i == 0:
        maior = valor
    if valor > maior:
        maior = valor
        posicao = i

print(num)
print(f"O maior número é: {maior}")
print(f"A posição do maior número é: {posicao}")
