'''
Crie um programa que:
1. Use for
2. Conte de 1 a 50
3. Use continue para pular os múltiplos de 5
'''
for i in range(1, 51):
    if i % 5 == 0:
        continue
    print(i)