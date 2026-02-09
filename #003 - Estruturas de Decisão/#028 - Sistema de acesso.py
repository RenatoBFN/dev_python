'''
Crie:
    idade = 17
    tem_documento = True
    esta_acompanhado = False

Regras:

Pode entrar se:
    idade ≥ 18
    ou (idade < 18 e está acompanhado)
    E obrigatoriamente tem documento

Use if para imprimir:
    "Acesso permitido"
    "Acesso negado"
'''

idade = 17
tem_documento = True
esta_acompanhado = False

if (idade >= 18 or (idade < 18 and esta_acompanhado)) and tem_documento:
    print('Acesso permitodo')
else:
    print('Acesso negado')