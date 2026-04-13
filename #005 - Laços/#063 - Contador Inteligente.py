'''
Crie um programa que simule um contador inteligente:
1. Usuário informa:
    início
    fim
    passo

O programa deve:
1. Validar entradas
2. Contar corretamente (crescente ou decrescente)
3. Não permitir passo zero
4. Usar for
5. Exibir cada valor da contagem
'''
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))

if passo == 0:
    passo = 1

print("\nContagem:\n")

if inicio < fim:
    for i in range(inicio, fim + 1, passo):
        print(i)
else:
    for i in range(inicio, fim - 1, -passo):
        print(i)