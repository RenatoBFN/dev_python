'''
Primeiro:
1. Faça um programa que percorra de 1 até 20 e:
    Se o número for múltiplo de 3, escreva: Fizz
2. Caso contrário:
    Mostre o número.
'''
for i in range (1, 21):
    if i % 3 == 0:
        print('Fizz')
    else:
        print(i)
