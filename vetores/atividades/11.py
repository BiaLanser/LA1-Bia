vet_num = []
maior = 0
menor = 0
posicao_maior = 0
posicao_menor = 0

for i in range(5):
    num = int(input(f"Digite um número: "))

    if i == 0:
        maior = num
        menor = num
    if maior < num:
        maior = num
        posicao_maior = i
    elif num < menor:
        menor = num
        posicao_menor = i

print(f"""
A posição do maior número é: {posicao_maior}
A posição do menor número é: {posicao_menor}
""")
