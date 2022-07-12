lado_1 = float(input("Digite o 1º lado do triângulo: "))
lado_2 = float(input("Digite o 2º lado do triângulo: "))
lado_3 = float(input("Digite o 3º lado do triângulo: "))

if lado_1 == lado_2 and lado_2 == lado_3:
    print("o Triângulo é equilátero ")
elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
    print("O triânguço é isóceles")
else:
    print("O triângulo é escaleno")

