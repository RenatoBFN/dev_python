'''
Crie um programa que:
1. Receba um número decimal (float)
2. Mostre:
    Parte inteira
    Parte decimal separada
    Número arredondado
    Número truncado (sem arredondar)
'''
number_float = 5.15

print(f'Parte Inteira: {int(number_float)}\n'
      f'Parte Decimal: {number_float - int(number_float):.2f}\n'
      f'Arredondado..: {round(number_float)}\n'
      f'Truncado.....: {abs(number_float)}')