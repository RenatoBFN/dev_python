'''
Uma empresa aplica reajuste salarial baseado no salário atual:
    Até 1500 → +20%
    1501 até 3000 → +15%
    3001 até 5000 → +10%
    Acima de 5000 → +5%

O programa deve mostrar:
1. Salário antes
2. Percentual aplicado
3. Valor do aumento
4. Novo salário
'''
antigo_sal = int(input('Salário do Representante: '))

if antigo_sal < 1500:
    novo_sal = antigo_sal * (20 / 100)
elif antigo_sal >= 1501 or antigo_sal <= 3000:
    novo_sal = (antigo_sal * 100 / 15)
elif antigo_sal >= 3001 or antigo_sal <= 5000:
    novo_sal = (antigo_sal * 100 / 10)
else:
    novo_sal = (antigo_sal * 100 / 5)

print(novo_sal)