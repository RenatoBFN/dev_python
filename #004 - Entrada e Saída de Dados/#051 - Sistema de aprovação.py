'''
Crie um programa que:
1. Peça o nome do aluno
2. Peça nota e frequência
3. Converta os valores corretamente
4. Regras:
    Aprovado se nota ≥ 7 e frequência ≥ 75
    Use if / else

Mostre o resultado com f-string
'''

nome = input('Digite o seu nome e sobrenome: ')
nota = float(input('Digite a sua nota: '))
frequencia = float(input('Quantidade de aulas assistida no mês: '))

freq_porcentagem = (frequencia / 30) * 100

if (nota >= 7 and freq_porcentagem >= 75.00):
     print('\nAprovado')
else:
    print('\nReprovado')
