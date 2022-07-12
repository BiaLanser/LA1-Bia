soma_numeros = 0
while True:
    valor_digitado = int(input("Digite qualquer número ou 0 para sair: "))
    
    if not valor_digitado:
        break

    soma_numeros += valor_digitado

print(f"A soma dos números digitados é: {soma_numeros}")
print("Finalizou o programa")