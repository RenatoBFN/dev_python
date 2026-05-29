'''
Crie um programa que:

1. Peça a nota do aluno (0 a 10)
2. Mostre:
    Nota maior ou igual a 7 → Aprovado
    Nota entre 5 e 6.9 → Recuperação
    Nota menor que 5 → Reprovado
    Se a nota for menor que 0 ou maior que 10: Nota inválida
'''
nome = input('Digite o primeiro nome do aluno: ')
nota = float(input(f'Digite a nota do {nome}: '))

if nota < 5:
    print(f'{nome} está REPROVADO!')
elif nota >= 5 or nota <= 6.9:
    print(f'{nome} está de RECUPERAÇÃO!')
elif nota >= 7:
    print(f'{nome} está APROVADO!')
else:
    print('NOTA DIGITADA NÃO ATENDE AOS CRITÉRIOS DE AVALIATIVO!')