'''
Crie:
    tem_cartao = False
    tem_dinheiro = False


Crie uma variável booleana que represente:

1. NÃO (tem cartão OU tem dinheiro)

Imprima o resultado.
'''

tem_cartao = False
tem_dinheiro = False

resultado = (not tem_cartao) or (not tem_dinheiro)

print(f'Existe meios de pagamento: {resultado}')