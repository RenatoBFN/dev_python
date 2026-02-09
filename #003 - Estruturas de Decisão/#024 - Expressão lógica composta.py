'''
Crie:
    nota = 6
    frequencia = 80

Aprovado se:

1. nota ≥ 7 ou
2. nota ≥ 6 e frequência ≥ 75

Use if para validar.
'''

nota = 6
frequencia = 75

if nota >= 7 or (nota >= 6 and frequencia >= 75):
    print('Aprovado!')
else:
    print('Reprovado!')