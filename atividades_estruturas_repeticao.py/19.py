soma_notas = 0

while True:
    codigo = int(input("Digite o código do aluno: "))

    if codigo == 0:
        print("Programa encerrado!")
        break
    
    for d in range (3):
        notas = float(input(f"Digite sua {d + 1}ª nota: "))
        soma_notas += notas

    media = soma_notas / 3
    
    print(f"A média do aluno com a matrícula {codigo} é {media}")

