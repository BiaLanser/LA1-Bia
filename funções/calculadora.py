def somar(num_1: int, num_2: int) -> int:
    """A função retorna a soma de 2 números"""
    return num_1 + num_2

def subtrair(num_1: int, num_2: int) -> int:
    """A função retorna a subtração de 2 números"""
    return num_1 - num_2

def multiplicar(num_1: int, num_2: int) -> int:
    """A função retorna a multiplicação de 2 números"""
    return num_1 * num_2

def dividir(num_1: int, num_2: int) -> float:
    """A função retorna a divisão de 2 números"""
    return num_1 / num_2

print(somar(10, 2))
print(subtrair(10, 2))

#Fazer 2 operações:

resultado = somar(10, 2) + subtrair(10, 2)
print(resultado)

print(multiplicar(10, 2))
print(dividir(10, 2))

def mostra_menu() -> str:
    return input("""
    Calculadora com Funções:

    1) Somar
    2) Subtrair
    3) MUltiplicar
    4) Dividir
    5) Sair

    Opção escolhida:
    """)



while True:
    opcao = mostra_menu()

    if opcao == "5":
        break

    num_1 = int(input("Digite o número 1: "))
    num_2 = int(input("Digite o número 2: "))

    resultado = None
    if opcao == "1":
        resultado = somar(num_1, num_2)
    elif opcao == "2":
        resultado = subtrair(num_1, num_2)
    elif opcao == "3":
        resultado = multiplicar(num_1, num_2)
    elif opcao == "4":
        resultado = dividir(num_1, num_2)

    if not resultado:
        print("Opção inválida")
        continue

    print(f"O resultado da operação é: {resultado}")
    