"""
21) Faça um script que receba o nome de cinco produtos e seus respectivos preços,
armazene­-os em dois vetores separados, um para os produtos e outro para os preços.
O programa deve calcular e mostrar:
a) A quantidade de produtos com preço inferior a R$ 50,00;
b) O nome dos produtos com preço entre R$ 50,00 e R$ 100,00;
c) A média dos preços dos produtos com preço superior a R$ 100,00.
"""
vet_preco = []
vet_produto = []
produto_entre_50_e_100 = []
qtde_num = 0
med = []

for i in range(5):
    produto = (input(f"Digite o nome do {i + 1}º produto: "))
    vet_produto.append(produto)
    preco = int(input(f"Digite o valor do preço {i + 1}º produto: "))
    vet_preco.append(preco)

    if preco < 50:
        qtde_num += 1
    
    elif preco >= 50 and preco <= 100:
        produto_entre_50_e_100.append(produto)

    else:
        med.append(preco)

media = sum(med) / len(med)

print(f"""
A quantidade de produtos com preço inferior a R$ 50,00 é: {qtde_num}
Os produtos com preço entre R$ 50,00 e R$ 100,00 é: {produto_entre_50_e_100}
A média dos preços dos produtos com preço superior a R$ 100,00 é: {media}
""")