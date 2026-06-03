'''
Crie um programa que:
1. Peça 5 números ao usuário
2. Use for

Mostre:
1. maor número
2. menor número
'''
for i in range(5):
    numero = int(input('Digite um número: '))
    
    if i == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        
        if numero < menor:
            menor = numero

print(f'Maior número: {maior}')
print(f'Menor número: {menor}')