a = float(input("Digite seu 1º número: "))
b = float(input("Digite seu 2º número: "))
c = float(input("Digite seu 3º número: "))

if a - b > 0 and a - c > 0 and b - c > 0:
    maior_num = a
    medio_num = b
    menor_num = c
elif a - b > 0 and a - c > 0 and b - c < 0:
    maior_num = a
    medio_num = c
    menor_num = b
elif a - b < 0 and a - c > 0 and b - c > 0:
    maior_num = b
    medio_num = a
    menor_num = c
elif a - b < 0 and a - c < 0 and b - c > 0:
    maior_num = b
    medio_num = c
    menor_num = a
elif a - b > 0 and a - c < 0 and b - c < 0:
    maior_num = c
    medio_num = a
    menor_num = b
else:
    maior_num = c
    medio_num = b
    menor_num = a




print(maior_num, medio_num, menor_num)

