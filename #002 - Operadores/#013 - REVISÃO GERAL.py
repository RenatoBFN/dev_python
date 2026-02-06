'''
Crie um programa que:

1. Use comentários
2. Crie variáveis dos tipos:
    int
    float
    str
    bool
3. Use:
    Operadores aritméticos
    Operadores de comparação
    Operadores lógicos
    Autoatribuição

Imprima todos os resultados de forma organizada
'''

print('RESUMO DA UNIDADE\n')

number_int = 10
number_float = 9.8
txt_str = 'Concluído'
result = True

print(f'A soma dos números: {number_int + number_float:.2f}\n'
      f'A subtração dos números: {number_int - number_float:.2f}\n'
      f'A multriplicação dos números: {number_int * number_float:.2f}\n'
      f'A divisão dos números: {number_int / number_float:.2f}\n'
      f'Os números são iguais?: {number_int == number_float}\n'
      )

print(f'Aluno está aprovado? (True = Aprovado / False = Reprovado)\n'
      f'Resultado: {txt_str == 'Concluído' and result}\n'
      )

number_int += 5

print(f'Nota final: {number_int}')