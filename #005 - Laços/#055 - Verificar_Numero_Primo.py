'''
Crie um programa que:
1. Peça um número ao usuário
2. Use for para verificar se ele é primo
3. Mostre se é primo ou não
'''
number = int(input('Digite um número: '))

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(number, 'não é primo')
            break
    else:
        print(number, 'é primo')