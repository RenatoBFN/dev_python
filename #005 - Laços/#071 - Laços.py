'''
Crie um programa que:
1. Peça números ao usuário até ele digitar "sair"
2. Calcule:
    soma
    quantidade de números
    maior
    menor
3. Mostre apenas os números ímpares
4. Ignore números negativos (continue)
'''
numero = 0

while True:
    entrada = input('Digite os números para o cálulo e digite "SAIR" para finalizar: ')

    if entrada.strip().lower() == 'sair':
        break

    dados = int(entrada)
    numero += dados

print(f'\nResultado: {numero}')

contador = dados
contador += 1

print(f'Total de números digitados: {contador}')

