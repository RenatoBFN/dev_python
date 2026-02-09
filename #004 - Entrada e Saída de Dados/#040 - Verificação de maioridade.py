'''
Crie um programa que:
1. Peça a idade do usuário
2. Converta para int
3. Use if / else para imprimir:
    "Maior de idade"
    "Menor de idade"
'''

idade = int(input('Digite a sua idade: '))

if idade < 18:
    print('\nMenor de idade.')
else:
    print('\nMaior de idade.')