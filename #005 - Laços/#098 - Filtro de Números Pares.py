'''
Crie um programa que:
1. Mostre os números de 1 até 20.
2. Ignore todos os números pares utilizando: continue
'''
for i in range(1, 21):
    if i % 2 == 0:
        continue
    print(i)