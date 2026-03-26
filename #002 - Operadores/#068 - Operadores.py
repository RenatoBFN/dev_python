'''
Crie um programa que:
1. Peça dois números
2. Mostre:
    soma
    multiplicação
    divisão
3. Mostre se:
    o primeiro é maior que o segundo
    os números são iguais
4. Verifique se:
    ambos são maiores que 10
'''
number1 = int(input('Digite o primeiro número: '))
number2 = int(input('Digite o segundo número: '))

print('\nCálculo dos números:\n'
      f'SOMA.........: {number1 + number2}\n'
      f'MULTIPLICAÇÃO: {number1 * number2}'
      )

if number2 != 0:
    print(f'DIVISÃO......: {number1 / number2:.1f}\n')
else:
    print('DIVISÃO......: Não é possível dividir por zero\n')

if number1 > number2:
    print('O primeiro número é maior que o segundo.\n')
elif number1 == number2:
    print('Os números são iguais.\n')
else:
    print('O primeiro número é menor que o segundo.\n')

if number1 > 10 and number2 > 10:
    print('Os números são maiores que 10.')
else:
    print('Um dos números ou os dois números não são maiores que 10.')