'''
Crie:
    idade = 16
    esta_acompanhado = False


Regra:

Acesso NEGADO se
NÃO (idade ≥ 18 OU está acompanhado)

Use not no bloco inteiro, não em partes isoladas.

Imprima:
1. "Acesso negado"
2. "Acesso permitido"
'''

idade = 16
esta_acompanhado = False

validador = not (idade >= 18 or esta_acompanhado)

if validador:
    print('Acesso negado')
else:
    print('Acesso permitido')