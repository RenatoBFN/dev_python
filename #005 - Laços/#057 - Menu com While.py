'''
Crie um programa que:
1. Use while

Simule um menu:
1 - Olá
2 - Contar até 5
0 - Sair

Só encerre quando o usuário escolher 0
'''
while True:
    print('Menu de Opções::\n'
      '( 1 ) - Olá\n'
      '( 2 ) - Contar até 05\n'
      '( 0 ) - Sair do Sistema\n')

    opcao = int(input('Digite a opção deseja: '))
    
    if opcao == 1:
        print('Olá\n')
    elif opcao == 2:
        print('1, 2, 3, 4, 5...\n')
    elif opcao == 0:
        break
    else:
        print('Digite uma opção correta!\n')