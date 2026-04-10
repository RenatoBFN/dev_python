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
soma = 0
contador = 0

while True:
    entrada = input('Digite um número ou "sair": ').strip().lower()
    
    if entrada == 'sair':
        break
    
    try:
        numero = int(entrada)
    except:
        print('Digite apenas números ou "sair"')
        continue
    
    if numero < 0:
        continue
    
    soma += numero
    contador += 1
    
    if contador == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        
        if numero < menor:
            menor = numero
    
    if numero % 2 != 0:
        print(f'Ímpar: {numero}')

if contador > 0:
    media = soma / contador

    print('\nRESULTADOS:')
    print(f'Soma: {soma}')
    print(f'Quantidade: {contador}')
    print(f'Maior: {maior}')
    print(f'Menor: {menor}')
    print(f'Média: {media:.2f}')
else:
    print('Nenhum número válido foi digitado.')

