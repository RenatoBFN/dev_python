'''
Crie um programa que:
1. Peça:
    nome
    salário
2. Mostre:
    salário com aumento de 10%
3. Pergunte:
    "Deseja ver o valor anual? (S/N)"
4. Se sim:
    mostre salário anual
5. Se não:
    finalize
'''
nome = input('NOME..: ')
salario = float(input('SALÁRIO: '))

aumento = 10.00
sal_aumento = aumento / 100 * salario
total_sal = sal_aumento + salario

print(f'\n VOCÊ RECEBERÁ UM AUMENTO DE: R${sal_aumento}')
print(f' Seu novo salário é de: R${total_sal}')

consulta = input('\nDeseja ver o valor anual? (S/N): ')

if consulta.strip().lower() == 's':
    print(f'O valor anual é de: R${total_sal * 12:.2f}')
else:
    print('Programa Encerrado...')