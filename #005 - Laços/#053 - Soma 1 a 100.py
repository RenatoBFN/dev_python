'''
Crie um programa que:
1. Use for
2. Some todos os números de 1 a 100
3. Mostre o resultado final
'''
number = 0

for i in range(1, 101):
    number += i

print(f'A soma de todos os números de 1 a 100 é: {number}')