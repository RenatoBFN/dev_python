'''
Crie duas versões da mesma condição:

Uma usando not (A and B)
Outra usando a forma simplificada

Compare os resultados imprimindo ambos.
'''

tem_acesso = True
tem_documento = False

resultado_1 = not (tem_acesso and tem_documento)

resultado_2 = (not tem_acesso) or (not tem_documento)

print(f'Resultado 1: {resultado_1}')
print(f'Resultado 2: {resultado_2}')