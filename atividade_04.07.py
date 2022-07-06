#2
from audioop import bias
import math
from re import A


nome = "Bia"
print(f"Olá, meu nome é {nome}")

#3

input("""

Cadastro de funcionários

a) Cadastrar funcionários
b) Listar funcionários
c) Editar funcionário
d) Remover funcionário
e) Sair
"Digite a opção desejada:
""")

#4

admin = "João"
nome = "João"
print(nome)

#5

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura  = float(input("Digite sua altura : "))
telefone = (input("Digite seu telefone: "))

print(f"""
Nome: {nome}
Idade: {idade}
Peso: {peso}
Altura: {altura}
Telefone: {telefone}
""")

#6

titulo= "Os Amadores"
edicao= "1ª edição"
autor= "Sara Shepard"
data_publicacao= "10/07/2020"

print(f"""
Título: {titulo}
Edição: {edicao}
Autor: {autor}
Data de publicação: {data_publicacao}
""")

#7

born_date = "2005-12-25"
child_amount = 0
user_name = "Bia"

#9

x = 10
y = 8
area = (x * y) / 2 + 3 ** 4

print(area)

#11

altura = float(input("Qual a altura do retângulo: "))
largura = float(input("Qual a largura do retângulo: "))

area = altura*largura
perimetro = (largura * 2) + (altura * 2)

print(f"""
Área: {area}
Perímetro: {perimetro}
""")

#12

num1=int(input("Digite seu 1º número: "))
num2=int(input("Digite seu 2º número: "))

print(f"A soma dos seus números é {num1 + num2}")

#13

nota1 = int(input("Digite sua 1ª nota: "))
nota2 = int(input("Digite sua 2ª nota: "))
print(f"A sua média será {(nota1 + nota2)/2:.2f}")

#14

number1= int(input("Type your 1st number: "))
number2= int(input("Type your 2nd number: "))
number3= int(input("Type your 3rd number: "))

squared1 = number1 ** 2
squared2 = number2 ** 2
squared3 = number3 ** 2

print(f"""
The squared of that numbers is: 

{number1} = {squared1}
{number2} = {squared2}
{number3} = {squared3}
""")

#15

A=10
B=20
A, B = B, A
print(A, B)

#16

months_amout = int(input("Type de amount of months: "))

days_amount = months_amout * 30
print(f"The amout of days in that months is {days_amount}")
