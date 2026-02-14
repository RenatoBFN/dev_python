'''
Crie um programa que peça um número ao usuário e imprima a tabuada desse número (1 a 10) usando for.
'''
print('Calculadora - Tabuada\n')
number = int(input('Qual o número que deseja calcular?: '))

for i in range (1,11):
    i *= number
    print(i)