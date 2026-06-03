nome = input('Nome do Aluno: ')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2) / 2

if media >= 7:
    print(f'O {nome} ficou com a média {media}. Situação: Aprovado')
else:
    print(f'O {nome} ficou com a média {media}. Situação: Reprovado')