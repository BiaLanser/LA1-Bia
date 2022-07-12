vetor_1 = []
vetor_2 = []
vetor_soma = []
vetor_diferenca = []
vetor_multiplicacao = []

for i in range (3):
    valor_1 = int(input(f"Digite o {i + 1} valor so vetor 1: "))
    valor_2 = int(input(f"Digite o {i + 1} valor so vetor 2: "))

    vetor_1.append(valor_1)
    vetor_2.append(valor_2)
    vetor_soma.append(valor_1 + valor_2)
    vetor_diferenca.append(valor_1 - valor_2)
    vetor_multiplicacao.append(valor_1 * vetor_2)

print(f"""
Vetor 1: {vetor_1}
Vetor 2: {vetor_2}
Vetor soma: {vetor_soma}
Vetor Diferença: {vetor_diferenca}
Vetor multiplicação: {vetor_multiplicacao}
""")