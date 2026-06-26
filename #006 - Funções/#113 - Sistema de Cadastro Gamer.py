'''
Crie um programa que cadastre um personagem.

1. Pergunte:
    Nome do personagem
    Classe

2. Crie uma função:
    def gerar_status():

3. Crie uma função que retorne uma mensagem personalizada:
    def mensagem_boas_vindas(nome, classe):

Exemplo:

Bem-vindo Renato!
Sua classe escolhida foi Guerreiro.
Você inicia com 100 pontos de vida.

4. Exiba tudo usando os retornos das funções.
'''
print('⁺˚⋆｡°✩₊✩°｡⋆˚⁺⁺˚⋆｡°✩₊✩°｡⋆˚⁺⁺˚⋆｡°✩₊✩°｡⋆˚⁺')
print('       Bem-vindos ao ChatGPT            ')
print('⁺˚⋆｡°✩₊✩°｡⋆˚⁺⁺˚⋆｡°✩₊✩°｡⋆˚⁺⁺˚⋆｡°✩₊✩°｡⋆˚⁺')
classe = int(input('( 1 ) ARQUERIO\n'
               '( 2 ) GUERREIRO\n'
               '( 3 ) MAGO\n'
               'ESCOLHA SUA CLASSE: '))
nome = input('NOME DE PERSONAGEM: ')

def gerar_status(atributos):
    if atributos == 1:
        return f'Atributos de classe ARQUEIRO:\nVitalidade: 150\nEnergia...: 120\nForça.....: 180'
    elif atributos == 2:
        return f'Atributos de classe GUERREIRO:\nVitalidade: 180\nEnergia...: 150\nForça.....: 120'
    else:
        return f'\nAtributos de classe MAGO:\nVitalidade: 120\nEnergia...: 180\nForça.....: 150'
status = gerar_status(classe)

def mensagem_boas_vindas(persona, profissao):
    return f'\nBem-vindo {persona}\n{profissao}'

print(mensagem_boas_vindas(nome, status))



