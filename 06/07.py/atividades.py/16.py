gols_time_1 = int(input("Quantos gols o 1º time fez? "))
gols_time_2 = int(input("Quantos gols o 2º time fez? "))

if gols_time_1 > gols_time_2:
    print("O 1º time ganhou")
elif gols_time_1 < gols_time_2:
    print("O 2º time ganhou")
else:
    print("O jogo terminou em empate")