idade = int(input("Qual a sua idade? "))

if idade < 18 or idade > 67:
    print("Você não tem idade para efetuar a doação de sangue")
else:
    print("Você poderá efetuar a doação de sangue")