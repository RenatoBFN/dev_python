'''
Agora as regras são:
Se for múltiplo de 3 e 5, mostrar: FizzBuzz
Senão, se for múltiplo de 3, mostrar: Fizz
Senão, se for múltiplo de 5, mostrar: Buzz
Caso contrário, mostrar o número.
'''
for i in range (1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)