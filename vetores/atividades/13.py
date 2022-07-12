vet_notas = []

qtde_alunos = int(input("Quantos alunos tem na sala: "))

for i in range(qtde_alunos):
    nota = float(input(f"Digite o nota do {i + 1}º aluno: "))
    vet_notas.append(nota)

    if nota > 0:
        continue
    else:
        break

media = sum()
print(f"""
Média da turma: {media}
""")