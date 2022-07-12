num = []
negativos = []
positivos = []

for i in range(4):
    numero = int(input(f"Digite seu {i + 1}º número: "))
    num.append(numero)
    
    if numero >= 0:
        positivos.append(numero)
    else:
        negativos.append(numero)

soma_positivos = sum(positivos)

print (f"""
Seus números foram: {num}
a quantidade de números negativos é: {len(negativos)}
A soma dos números positivos é: {soma_positivos}
""")