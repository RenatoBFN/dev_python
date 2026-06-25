'''
Crie um programa que:
1. Peça:
    Nome do aluno
    Nota 1
    Nota 2
    Nota 3
2. Crie uma função que retorne a média:
    def calcular_media(n1, n2, n3):
3. Crie outra função:
    def verificar_situacao(media):
que retorne:
    APROVADO - se a média for maior ou igual a 7:
    RECUPERAÇÃO - se a média for entre 5 e 6.9.
    REPROVADO - se a média for menor que 5.
4. Exiba um relatório.
'''
print('*' * 30)
print(' BOLETIM ESCOLAR ')
print('*' * 30)
nome = input('Nome do ALUNO: ')
n1 = float(input('Primeira NOTA: '))
n2 = float(input('Segunda NOTA.: '))
n3 = float(input('Tereira NOTA.: '))

def notas(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3
media = notas(n1, n2, n3)


def status(verif_final):
    if verif_final >= 7:
        return 'Aluno(a) Aprovado!'
    elif verif_final >= 5 and verif_final <= 6.9:
        return 'Aluno(a) em Recuperação!'
    else:
        return 'Aluno Reprovado!'
resultado = status(media)

print('*' * 30)
print(f'Aluno(a) {nome}')
print(f'Matemática: {n1:.2f}.\n'
      f'Ciências..: {n2:.2f}.\n'
      f'Português.: {n3:.2f}.\n')
print(f'Nota Final: {media:.2f}.\n'
      f'Status....: {resultado}.')