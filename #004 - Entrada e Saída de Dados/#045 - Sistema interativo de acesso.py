'''
Crie um programa que:

1. Peça:
    Idade
    Se está acompanhado (sim ou não)
    Se tem documento (sim ou não)
2. Converta as respostas para valores booleanos
3. Regra:
    Pode entrar se:
        idade ≥ 18
        ou (idade < 18 e está acompanhado)
    E obrigatoriamente tem documento
4. Use:
    input()
    conversão de tipos
    operadores lógicos
    if / else
5. Imprima:
    "Acesso permitido"
    "Acesso negado"
'''

idade = int(input('IDADE: '))
acompanhado = input('ACOMPANHADO? (S = Sim / N = Não): ')
documento = input('Está com documentos? (S = Sim / N = Não): ')

if acompanhado == 'S' or acompanhado == 's':
    acompanhado = True
else:
    acompanhado = False

if documento == 'S' or documento == 's':
    documento = True
else:
    documento = False

if (idade >= 18 or (idade < 18 and acompanhado)) and documento:
    print('Acesso Permitido')
else:
    print('Acesso Negado')