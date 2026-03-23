'''
Crie um programa que:
1. Use while
2. Peça números ao usuário
3. Pare somente quando o usuário digitar 0
4. Mostre quantos números foram digitados (exceto o 0)
'''
number = 0

while True:
    valor = int(input('Digite um número: '))
    if valor == 0:
        break
    number += 1
   
print(f'Quantidade de números digitados: {number}')