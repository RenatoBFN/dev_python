'''
🎯 Atividade — Classificador de Candidato
Crie um programa que avalie um candidato para uma vaga.
O programa deve pedir:
Nome do candidato.
Idade.
Anos de experiência.
Se possui ensino superior (S ou N).
Regras de avaliação
APROVADO se:
idade maior ou igual a 18;
experiência maior ou igual a 2 anos;
ensino superior = S.
ENTREVISTA TÉCNICA se:
idade maior ou igual a 18;
experiência entre 1 e 1,9 ano;
ensino superior = S.
BANCO DE TALENTOS se:
idade maior ou igual a 18;
ensino superior = N;
experiência maior ou igual a 2 anos.
REPROVADO para qualquer outro caso.
'''

print('*' * 25)
print('    DADOS DO CANDIDATO')
print('*' * 25)

nome = input('NOME: ')
idade = int(input('IDADE: '))
time_exp = int(input('TEMPO DE EXP.: '))
graduado = input('Graduado? (s = sim , n = não): ')