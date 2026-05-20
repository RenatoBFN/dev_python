'''
Crie um programa que:
1. Pergunte o salário do funcionário
2. Aplique um reajuste de 10%

Mostre:
1. salário antigo
2. valor do aumento
3. novo salário
'''
antigo_sal = int(input('Salário do Representante: '))
porc_aumento = int(input('De quanto será o aumento de salário: '))

novo_sal = antigo_sal * porc_aumento / 100

print(f'\nO antigo salário era de: R${antigo_sal:.2f}')
print(f'O aumento será de: R${novo_sal:.2f}')
print(f'Seu novo salário é de: R${antigo_sal + novo_sal:.2f}')