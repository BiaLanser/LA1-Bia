turno = input("""

Digite seu turno:

M-Matutino
V-Vespertino
N-Noturno

""")

if turno == "M":
    print("Bom dia!")
elif turno == "m":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "v":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
elif turno == "n":
    print("Boa noite!")
else:
    print("Opção inválida")