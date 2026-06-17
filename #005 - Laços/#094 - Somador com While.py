'''
Crie um programa que:
1. Peça números inteiros ao usuário.
2. Continue pedindo números.
3. Quando o usuário digitar: 0. O programa encerra.
4. Mostre a soma de todos os números digitados.
'''
contador = 0

while True:
    numero = int(input('Digite um número inteiro: '))
    if numero == 0:
        break
    contador += numero

print(contador)