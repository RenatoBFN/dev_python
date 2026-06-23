'''
Crie uma função:
    somar(a, b)

que:
1. Receba dois números.
2. Retorne a soma deles.
3. Exiba o resultado usando print().

Exemplo:
    Digite o primeiro número: 10
    Digite o segundo número: 5
    Resultado: 15
'''
print('-' * 36 )
print('  Calculadora de Soma Gratuita')
print('-' * 36 )
primeiro_num = int(input('Digite o primeiro número inteiro: '))
segundo_num = int(input('Digite o segundo número inteiro.: '))

def somar(a, b):
    return a + b

print(f'\nResultado: {somar(primeiro_num, segundo_num)}')