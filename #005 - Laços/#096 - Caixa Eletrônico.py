'''
Crie um programa que:
1. Pergunte um valor para saque.
2. Se o valor digitado for: 0
   o programa deve mostrar: Operação cancelada.
   e encerrar imediatamente usando break.
3. Caso contrário, mostrar:
   Processando saque...
4. Continuar perguntando novos valores.
'''
contador = 0

while True:
    valor = int(input('Informe o valor para saque: '))
    if valor == 0:
        print('Operação Cancelada...')
        break
    else:
        print('Processando saque...')
        contador += 1
        print(f'Quantidade de Saques: {contador}')