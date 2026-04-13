'''
Crie um programa que:
1. Use while True
2. Peça números
3. Some todos
4. Pare quando o usuário digitar "sair"
5. Mostre a soma final
'''
soma = 0

while True:
    entrada = input("Digite um número ou 'sair': ")
    
    if entrada.lower() == 'sair':
        break
    
    numero = int(entrada)
    soma += numero

print(f"Soma total: {soma}")