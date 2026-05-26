'''
Crie um programa que:

Pergunte:
1. distância da viagem (km)
2. velocidade média (km/h)

Calcule:
3. tempo da viagem em horas
4. quantos minutos sobraram
'''
distancia = float(input('Qual a distância em KM? '))
velocidade = float(input('Qual a média de velocidade? (KM/h) '))

tempo_total = distancia / velocidade

horas = int(tempo_total)

minutos = (tempo_total - horas) * 60

print(f'\nDistância: {distancia:.0f}Km')
print(f'Velocidade: {velocidade:.0f}Km/h')

print(f'\nO tempo de viagem será de: {horas} horas e {minutos:.0f} minutos')


