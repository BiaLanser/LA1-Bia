vet_1 = []
vet_2 = []

for i in range(5):
    num = int(input(f"Digite seu {i + 1}º valor: "))
    vet_1.append(num)

vet_2 = vet_1[::-1]

print(f"""
O primeiro vetor é {vet_1}

E seu inverso é {vet_2}
""")