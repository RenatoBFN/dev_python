'''
Crie:

idade = 17
tem_autorizacao = True


Crie uma variável booleana que seja True se:

    idade ≥ 18 ou
    tem autorização

Imprima o resultado.
'''

idade = 17
tem_autorizacao = True 

validador = idade >= 18 or tem_autorizacao == True

print(f'O aluno está apto: {validador}.')