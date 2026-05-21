'''
Crie um programa que:

Pergunte:
1. distância da viagem (km)
2. velocidade média (km/h)

Calcule:
3. tempo da viagem em horas
4. quantos minutos sobraram
'''
distancia = int(input('Qual a distância em KM? '))
velocidade = int(input('Qual a média de velocidade? (KM/h) '))

tempo_viagem = distancia / velocidade
print(f'\nO tempo de viagem será de: {tempo_viagem:.0f}')
