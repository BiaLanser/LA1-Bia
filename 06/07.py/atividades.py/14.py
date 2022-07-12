import math


num = float(input("Digite um número: "))

if num >= 0:
    result = math.sqrt(num)
else:
   result = num * num
print(result)