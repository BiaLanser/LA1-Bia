habitantes = int(input("Quantos habitantes da cidade irão responder? "))
total_salario = 0
total_filhos = 0
maior_salário = 0

for i in range (habitantes):
    salario = float(input("Digite seu salário: "))
    if salario < 0:
        print("Valor inválido!")
    else:
        total_salario += salario

    if salario > maior_salário:
        maior_salario = salario
    else:
        continue

    filhos = int(input("Quantos filhos você tem? "))
    total_filhos += 1
media_salario = total_salario / habitantes
media_filhos = total_filhos / habitantes

print(f"""
Média salarial: {media_salario}
Média de filhos: {media_filhos}
Maior salário: {maior_salario}
""")
