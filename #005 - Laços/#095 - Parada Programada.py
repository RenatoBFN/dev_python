'''
Crie um programa que:
1. Mostre os números de 1 até 20.
2. Quando chegar no número 13:
    exiba a mensagem: Número de parada encontrado!
3. Interrompa o laço com break.
'''
for i in range (1, 21):
    if i == 13:
        print(i)
        print('\nNúmero de parada encontrado!')
        break
    print(i)