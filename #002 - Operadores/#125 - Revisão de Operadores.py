'''
Crie uma pequena Calculadora de Compra.

O programa deverá pedir ao usuário:

💰 Valor de um produto
🔢 Quantidade comprada
💸 Percentual de desconto

Depois, deverá calcular e apresentar:

Valor bruto da compra
valor × quantidade
Valor do desconto
Valor final após o desconto
Valor de cada parcela, considerando 3 parcelas
Informe também o resto da divisão do valor final por 3.
'''


valor = float(input('VALOR DO PRODUTO: '))
quantidade = int(input('QUANTIDADE: '))
desconto = float(input('% de DESCONTO: '))

preco_quantidade = valor * quantidade
calculo_desc = preco_quantidade * desconto / 100
valor_final = preco_quantidade - calculo_desc

print( '*' * 30)
print('       DADOS DA COMPRA')
print( '*' * 30)
print(f'PREÇO: R${valor:.2f} / QUANTIDADE: {quantidade}')
print(f'VALOR TOTAL: R${preco_quantidade:.2f}')
print(f'DESCONTO DO PRODUTO: R${calculo_desc:.2f}')
print(f'VALOR FINAL: R${valor_final:.2f}')

print(f'\nPARCELAMENTO: 3x R${valor_final / 3:.2f}')
print(f'\nRESTO R${valor_final % 3:.2f}')
