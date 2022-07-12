nomes = ["BIA", "JULIA", "ALEX", "JOÃO", "DARA"]

pessoa = input("Digite um nome: ")
pessoa = pessoa.upper()

if pessoa in nomes:
    print("ACHEI")
else:
    print("NÃO ACHEI")
