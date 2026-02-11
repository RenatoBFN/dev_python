'''
Crie um programa que:

1. Peça:
    Nome
    Idade
    Altura
2. Converta os tipos corretamente
3. Verifique se:
    Idade ≥ 18 → "Cadastro completo"
    Caso contrário → "Cadastro incompleto"

Exiba todas as informações organizadas
'''

nome = input('NOME..: ')
idade = int(input('IDADE.: '))
altura = float(input('ALTURA: '))

if idade >= 18:
    print(f'\nNOME..: {nome}\n'
          f'IDADE.: {idade}\n'
          f'ALTURA: {altura}\n'
          )
else:
    print('\nCadastro Incompleto!\n'
          'Refaça o Formulário\n'
          )