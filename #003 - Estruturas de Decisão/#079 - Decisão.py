'''
Crie um programa que:
1. Peça a idade do usuário
2. Classifique:
    menor de idade
    adulto
    idoso
3. Se for maior de 18:
    exiba: “Pode tirar habilitação”
4. Caso contrário:
    exiba: “Não pode tirar habilitação”
'''
idade = int(input('Digite a sua idade: '))

if 18 >= idade <= 59:
    print('Situação: Adulto\n'
          'Status..: Pode tirar habilitação'
          )
elif idade >= 60:
    print('Situação: Idoso\n'
          'Status..: Pode tirar habilitação'
         )
else:
    print('Situação: Menor de Idade\n'
          'Status..: Não Pode tirar habilitação'
         ) 