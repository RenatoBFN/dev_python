'''
Um sistema precisa decidir se uma pessoa pode entrar em um evento.

Regras:
1. A pessoa pode entrar se:
    idade ≥ 18
    ou (idade < 18 e está acompanhada)
2. Em qualquer caso, é obrigatório ter documento

Requisitos do programa:
1. Criar variáveis:
    idade
    esta_acompanhado
    tem_documento
2. Usar:
    operadores lógicos (and, or, not)
    parênteses para controle da lógica
    if / else
3. Imprimir:
    "Acesso permitido"
    "Acesso negado"
'''

idade = 15
esta_acompanhado = True
tem_documento = False

if (idade >= 18 or (idade < 18 and esta_acompanhado)) and tem_documento:
    print('Acesso Permitido')
else:
    print('Acesso Negado')