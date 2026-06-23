'''
Crie uma função:
    calcular_desconto(valor)

que:
1. Receba o valor de um produto.
2. Retorne o valor com 10% de desconto.
3. Mostre o resultado formatado com duas casas decimais.

Exemplo:
    Digite o valor do produto: 100

    Valor com desconto: R$90.00
'''
print('-' * 32 )
print('  Calculadora de Desconto')
print('-' * 32 )
valor_produto = float(input('Digite o valor do produto: '))
porcentagem_desc = 10

def calcular_desconto(valor):
    return valor * (porcentagem_desc / 100)

preco_final = valor_produto - calcular_desconto(valor_produto)

print(f'\nO valor de desconto é de: R${calcular_desconto(valor_produto):.2f}')
print(f'Valor para pagamento: R${preco_final:.2f}')