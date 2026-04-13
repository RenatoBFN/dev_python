'''
Crie um programa que:
1. Use variáveis
2. Use condições (if/else)
3. Use for
4. Use while
5. Use break ou continue
6. Use input()

📌 O programa deve:
1. Pedir ao usuário quantos números ele quer digitar
2. Ler esses números

Mostrar:
    soma
    média
    maior
    menor
'''
soma = 0
contador = 0

while True:
    entrada = input('Digite um número ou "sair": ')
    
    if entrada.lower() == 'sair':
        break
    
    numero = int(entrada)
    
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

media = soma / contador

print(f'\nSoma: {soma}')
print(f'Média: {media}')
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')