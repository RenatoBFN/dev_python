'''
Crie:
    usuario_bloqueado = False

Use if e not para permitir ou negar acesso.
'''

usuario_bloqueado = True

usuario_bloqueado = not False

if usuario_bloqueado:
    print('Liberado!')
else:
    print('Bloqueado')