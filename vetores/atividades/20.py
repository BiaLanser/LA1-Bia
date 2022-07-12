vet_notas = []
notas_acima_media = []

for i in range(10):
    nota = int(input(f"Digite a {i + 1}ª nota: "))
    vet_notas.append(nota)

    if nota > 5.9:
        notas_acima_media.append(nota)
    elif nota < 0:
        print("Nota inválida!")
 
media = sum(vet_notas) / len(vet_notas)

print (f"""
A média das notas da turma é: {media}
As notas acima da média foram: {notas_acima_media}
""")