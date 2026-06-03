'''
Crie uma variável idade.
Use if / elif / else para classificar:

1. Menor que 18 → "Jovem"
2. Entre 18 e 65 → "Adulto"
3. Maior que 65 → "Idoso"
'''

idade = 66

if idade < 18:
    print('Jovem')
elif idade >= 18 and idade <= 65:
    print('Adulto')
else:
    print('Idoso')