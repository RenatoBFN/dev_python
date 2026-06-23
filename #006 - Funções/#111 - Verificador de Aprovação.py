'''
Crie uma função:
    avaliar_aluno(media)

que:
1. Retorne "APROVADO" se a média for maior ou igual a 7.
2. Retorne "RECUPERAÇÃO" se a média estiver entre 5 e 6.9.
3. Retorne "REPROVADO" se a média for menor que 5.

Depois:
1. Peça três notas.
2. Use uma função para calcular a média.
3. Use outra função para avaliar o aluno.
4. Mostre média e situação.
'''
print('*' * 30)
print(' BOLETIM ESCOLAR ')
print('*' * 30)
nome = input('Nome do ALUNO: ')
n1 = float(input('Primeira NOTA: '))
n2 = float(input('Segunda NOTA.: '))
n3 = float(input('Tereira NOTA.: '))

def avaliar_aluno(media):
    soma = n1 + n2 + n3
    return soma / 3

resultado_media = avaliar_aluno(n1 + n2 + n3)

def situacao_aluno(status):
    if avaliar_aluno(resultado_media) >= 7:
        print('Aluno(a) está !APROVADO!')
    elif avaliar_aluno(resultado_media) >= 5 and avaliar_aluno(resultado_media) <= 6.9:
        print('Aluno(a) está em !RECUPERAÇÃO!')
    else:
        print('Aluno(a) está !REPROVADO!')
    return

print(f'\nA média do alUno(a) {nome} é {avaliar_aluno(resultado_media):.2f}.')
avaliacao_final = situacao_aluno(resultado_media)


