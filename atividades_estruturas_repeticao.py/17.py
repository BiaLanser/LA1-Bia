jose = 0
maria = 0
joao = 0
nulo = 0
branco = 0
total = 0

print("""
1 - José Bolinha
2 - Maria Nascimento
3 - João da Silva
4 - Voto nulo
5 - Voto em branco

Digite "0" para finalizar a contagem
""")

while True:
    voto = int(input("Digite o seu voto: "))
    total += 1

    if voto == 0:
        break
    elif voto == "1":
        jose += 1
    elif voto == "2":
        maria += 1
    elif voto == "3":
        joao += 1
    elif voto == "4":
        nulo += 1
    elif voto == "5":
        branco += 1
    else:
        print("Valor Inválido!")
print(f"""
Total de Votos: {total}
José Bolinha: {jose}
Maria Nascimento: {maria}
João da Silva: {joao}
Votos nulos: {nulo}
Votos em branco: {branco}
""")
    
