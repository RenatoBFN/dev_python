'''
Crie uma função:
    calcular_media(nota1, nota2, nota3)

que:
1. Receba três notas.
2. Retorne a média delas.
3. Mostre o resultado com duas casas decimais.

Exemplo:
    Nota 1: 7
    Nota 2: 8
    Nota 3: 9

    Média: 8.00
'''
print('-' * 20)
print(' MÉDIA - 02° SEMETRE ')
print('-' * 20)
n1 = float(input('1° NOTA: '))
n2 = float(input('2° NOTA: '))
n3 = float(input('3° NOTA: '))

def calcular_media(nota1, nota2, nota3):
    soma = nota1 + nota2 + nota3
    return soma / 3

print(f'\nNota 4° Bimestre: {n1:.2f} '
      f'\nNota 5° Bimestre: {n2:.2f} '
      f'\nNota 6° Bimestre: {n3:.2f} ')

print(f'\nMédia Semestral: {calcular_media(n1, n2, n3):.2f}')

if calcular_media(n1, n2, n3) < 7:
    print('!Aluno REPROVADO!')
else:
    print('!Aluno APROVADO!')