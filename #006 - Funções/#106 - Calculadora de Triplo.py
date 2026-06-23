'''
Crie uma função chamada:
    triplo(numero)

que:
1. Receba um número.
2. Retorne o triplo dele usando return.
3. Mostre o resultado utilizando print().

Exemplo:
    Digite um número: 5
    Resultado: 15
'''
entrada_dados = int(input('Digite um número inteiro: '))

def triplo(numero):
    return numero * 3

print(f'Resultado (Triplo): {triplo(entrada_dados)}')