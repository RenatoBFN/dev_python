'''
1. Crie um programa que peça:
    Nome
    Idade
    Altura
    Cidade

E mostre uma ficha organizada na tela.
'''
nome = input('Digite seu nome...: ')
idade = int(input('Digite sua idade.: '))
altura = float(input('Digite sua altura: '))
cidade = input('Digite sua cidade: ')

print("=" * 15)
print(f'Nome..: {nome}\n'
      f'Idade.: {idade}\n'   
      f'Altura: {altura}\n'
      f'Cidade: {cidade}')
print("=" * 15)