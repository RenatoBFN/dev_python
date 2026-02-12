'''
Um jogo atribui pontos ao jogador ao longo da partida.

Requisitos do programa:
1. Criar uma variável pontos iniciando com valor 0
2. O jogador:
    Ganha 10 pontos
    Perde 3 pontos
    Ganha mais 5 pontos
3. Usar autoatribuição (+=, -=) para atualizar os pontos
4. Verificar:
    Se o total de pontos é par ou ímpar (usando %)
5. Exibir:
    Pontuação final
    Se o número é par ou ímpar
'''

jogador = 'Player 01'
score = 0

score += 10
score -= 3
score += 5

print(f'O jogador {jogador} tem: {score} pontos.\n')
print(f'O número é par: {score % 2 == 0}') # True == Par / False == Ímpar
