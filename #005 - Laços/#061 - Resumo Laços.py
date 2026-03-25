'''
Crie um programa que:
1. Use for
2. Use range(start, stop, step)
3. Use continue
4. Use break
5. Imprima apenas números ímpares
6. Pare o loop quando encontrar o número 15
'''
for i in range (1,102,2):
    if i == 3:
        continue
    if i == 17:
        break
    print(i)