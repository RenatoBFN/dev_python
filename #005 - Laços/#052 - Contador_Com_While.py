'''
Crie um programa que:
1. Use while
2. Peça números ao usuário
3. Pare somente quando o usuário digitar 0
4. Mostre quantos números foram digitados (exceto o 0)
'''
number = int(input('Digite um número: '))

while number != 0:
    number = int(input('Digite outro número: '))
    number +1
    if number == 0:
        break
print(f'Os números digitados foram: {number}')