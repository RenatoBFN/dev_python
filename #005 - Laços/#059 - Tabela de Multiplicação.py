'''
Crie um programa que:
1. Use for
2. Imprima uma tabela de multiplicação (1 a 5)

Exemplo:
    1 x 1 = 1
    1 x 2 = 2
'''
print('Tabuada do 1 ao 5!\n')

for i in range(1, 6):
    print(f'Tabuada do número {i}:') 
    for j in range(1, 11):  
        resultado = i * j
        print(f'{i} x {j} = {resultado}')
    print('-----------')