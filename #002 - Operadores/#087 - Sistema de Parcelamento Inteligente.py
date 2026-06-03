'''
Crie um programa que:

1. Pergunte:
    valor do produto
    quantidade de parcelas
2. Calcule:
    valor de cada parcela
    resto que sobra da divisão
'''
valor_prod = float(input('Qual é o valor do produto? '))
parcelas = int(input('Quantidade de parcelas: '))

print(f'\nO produto X foi vendido por R${valor_prod:.0f} em {parcelas} vezes.')

calc_parcela = valor_prod / parcelas
valor_parcela = int(calc_parcela)
parte_decimal = calc_parcela - int(calc_parcela)
centavos = parte_decimal * 100

print(f'\nResumo da Venda:')
print('Produto: X\n'
      f'Valor.: R${valor_prod:.0f}\n'
      f'Parcelamento: {parcelas}x\n'
      f'Valor Final.: {parcelas}x de R${valor_parcela},{centavos:.0f}')