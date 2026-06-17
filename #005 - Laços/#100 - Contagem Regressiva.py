'''
Crie um programa que:
1. Peça um número inteiro ao usuário.

Exemplo:

Digite um número: 8
Mostre uma contagem regressiva até 1.

Resultado:

8
7
6
5
4
3
2
1

Utilize: range() com passo negativo.
'''
numero = int(input('Diga um número inteiro para a contagem regressiva: '))

for i in range(numero, 0, -1):
    print(i)