'''
Crie uma função chamada:
    cumprimentar(nome)

que:
1. Receba um nome.
2. Retorne a frase:
    Olá, Renato! Seja bem-vindo.
3. O retorno deve ser exibido usando print() fora da função.

Exemplo:
    print(cumprimentar('Renato'))

Resultado:
    Olá, Renato! Seja bem-vindo.
'''
entrada_dados = input('Digite o seu primeiro nome: ')

def cumprimentar(nome):
    return f'Olá, {nome}! Seja bem-vindo'

print(cumprimentar(entrada_dados))