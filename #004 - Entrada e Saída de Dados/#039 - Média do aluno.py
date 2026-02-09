'''
Crie um programa que:
1. Peça o nome do aluno
2. Peça duas notas (float)
3. Calcule a média

Mostre o nome do aluno e a média formatada com 2 casas decimais
'''

nome = input('Digite o seu nome do aluno: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

print(f'\nAluno........: {nome}\n'
      f'Primeira nota: {nota1:.2f}\n'
      f'Segunda nota.: {nota2:.2f}\n'
      f'Média........: {(nota1 + nota2) / 2:.2f}'
       )