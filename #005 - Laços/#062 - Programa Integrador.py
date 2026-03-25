'''
Crie um programa que:
1. Use variáveis
2. Use condições (if/else)
3. Use for
4. Use while
5. Use break e continue
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
num1 = 35
num2 = 0
num3 = 15
num4 = 20

while True:
	entrada = input('Digite um ou vários números para a soma ou "sair": ')
	
	if entrada.lower() == "sair":
	    break

	numero = int(entrada)
	num2 += numero

print(f'A soma total dos número é de: {num2}.')

print('\nDos números digitados, nós teremos:')

a = 0
b = 0

for i in numero:
    numero = int(entrada)
    if i == 0:
        a = numero
        b = numero
    else:
        if numero > a:
            a = numero

        if numero < b:
            b = numero

print(f'Maior número: {a}')
print(f'Menor número: {b}')

print(f'\nMédia de todos os números do programa: {num1 + num2 + num3 + num4 / 4}.')

print('Apresentando os números pares digitados:\n')

for j in num2:
	if j % 2 == 0:
		continue
	print(j)