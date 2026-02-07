'''
Crie:

idade = 19
tem_documento = True
esta_acompanhado = False

Crie uma variável booleana que seja True se:

1. idade ≥ 18 ou
2. (idade < 18 e está acompanhado)

Depois, combine isso com:

1. tem_documento == True

Resultado final deve ser uma única variável booleana
Imprima o resultado.
'''

idade = 19
tem_documento = True
esta_acompanhado = False

validador = idade >= 18 or (idade < 18 and esta_acompanhado == True)

val_doc = validador and tem_documento == True

print(f'Resultado: {val_doc}')