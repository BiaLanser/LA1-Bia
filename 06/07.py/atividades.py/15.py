salario = float(input("Digite o seu salário: "))
emprestimo = float(input("Digite o valor de empréstimo desejado: "))

if emprestimo > (salario * .2):
    print("empréstimo não concedido")
else:
    print("empréstimo concedido")