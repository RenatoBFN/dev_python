'''
Crie uma função: def dobro(numero):

que:
Receba um número.
Retorne o dobro desse número usando return.
Guarde o resultado em uma variável.
Mostre o resultado com print().

Exemplo:

resultado = dobro(7)
print(resultado)

Saída: 14
'''
entrada_num = int(input('Digite um número inteiro: '))

def dobro(numero):
    return numero * 2

resultado = dobro(entrada_num)

print(resultado)