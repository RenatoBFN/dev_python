'''
Crie um programa que:
1. Use for
2. Conte de 1 a 50
3. Use continue para pular os múltiplos de 5
'''

number = 0  

for i in range(50):
    number += 1
    if number % 5 == 0:
        continue
    print(number)