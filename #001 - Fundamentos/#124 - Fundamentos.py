'''
Crie um pequeno "Cartão de Perfil".

O programa deverá pedir ao usuário:

Nome
Idade
Altura
Cidade onde mora
Se está estudando Python (True ou False)

Depois, apresente tudo de maneira organizada.
'''

nome = input('NOME: ')
idade = int(input('IDADE: '))
altura = float(input('ALTURA: '))
cidade = input('CIDADE: ')
curso_py = True

print( '=' * 21)
print('** FICHA CADASTRAL **')
print( '=' * 21)
print(f'NOME..: {nome}')
print(f'IDADE.: {idade}')
print(f'ALTURA: {altura}')
print(f'CIDADE: {cidade}')
print(f'CURSANDO PYTHON?: {curso_py}')
print( '=' * 21)
