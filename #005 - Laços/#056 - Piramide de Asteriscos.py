'''
Crie um programa que:
1. Use dois for (laços aninhados)
2. Imprima a seguinte saída:

    *
    **
    ***
    ****
    *****
'''
for i in range(1, 6):
    for j in range(i): 
        print('*', end='')
    print()


for i in range(1, 6):
    print(f"i vale: {i}")
    for j in range(i):
        print('*', end='')
    print()

    