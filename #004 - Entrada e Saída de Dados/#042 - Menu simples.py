'''
Crie um programa que:
1. Mostre um pequeno menu no terminal:
    Somar
    Subtrair
2. Peça a opção do usuário
3. Peça dois números
4. Execute a operação escolhida usando if / elif / else
5. Mostre o resultado
'''

print('\n---ESCOLHA UMA OPÇÃO---\n'
      '-----------------------\n'
      '1. SOMAR_______________\n'
      '2. SUBTRAIR____________\n'
      '-----------------------'
      )
opcao = int(input('Digita a opção..........: '))

if opcao == 1:
    print('\nVocê escolheu: SOMA')
elif opcao == 2:
    print(f'\nVocê escolheu: SUBTRAÇÃO')
else:
    print('\nVocê escolheu a opção do menu inválida - Escolha > 1 < (SOMAR) ou > 2 > (SUBTRAIR)...')
    opcao = int(input('Digita a opção..........: '))

number1 = float(input('Digite o primeiro número: '))
number2 = float(input('Digite o segundo número.: '))

if opcao == 1:
    print(f'\nResultado: {number1 + number2:.2f}')
elif opcao == 2:
    print(f'\nResultado: {number1 - number2:.2f}')
else:
    print('\nVocê escolheu a opção do menu inválida - Reinicie o sistema!')