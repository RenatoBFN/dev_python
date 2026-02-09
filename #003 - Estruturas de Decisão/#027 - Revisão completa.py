'''
Crie um programa que:

1. Use int, float, str, bool
2. Faça operações matemáticas
3. Use comparação
4. Use operadores lógicos
5. Use if / elif / else
6. Use autoatribuição

Imprima tudo de forma organizada
'''

# Variáveis
var_int = 10
var_float = 15.5
var_str = "Nova Fase"
var_bool = False

# Operações matemáticas
print(f'A soma dos números resulta em.....: {var_int + var_float:.2f}\n'
      f'A subtração dos números resulta em: {var_int - var_float:.2f}\n'
      )

# Comparação
print(f'Os resultados das operações dão o mesmo resultado?\n'
      f'Resposta: {(var_int + var_float) == (var_int - var_float)}\n'
      )

# Operadores Lógicos
if var_int >= 1 and var_float > var_int:
    print('O resultado da subtração poderá ser negativo.\n')
else:
    print('Não haverá resultado negativo.\n')

# Autoatribuição
var_int += 1

print(f'Novo resultado da variável inteiro: {var_int}\n')

# if / elif / else
print(f'A frase selecionada pelo programa é: {var_str}')
if var_str == "Nova Jornada":
    print('A mensagem selecionada está de acordo com o esperado.')
elif var_str == "Nova Fase":
    print('A mensagem está aceitável.')
else:
    print('Mensagem Incorreta.')