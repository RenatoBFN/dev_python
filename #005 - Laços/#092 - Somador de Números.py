'''
Crie um programa que:
1. Peça um número inteiro.
2. Mostre a soma de todos os números de 1 até ele.

Numero = int(input('Digite um número inteiro: '))
'''
numero = int(input('Digite um número inteiro: '))
soma = 0

for x in range(1, numero + 1):
    soma += x

print(soma)


