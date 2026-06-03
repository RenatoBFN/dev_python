'''
Crie um programa que:
1. Use input()
2. Converta tipos
3. Use print() e f-strings
4. Use if / else
5. Trabalhe com pelo menos:
    int
    float
    str
'''

nome = input('Digite o seu nome: ')
cidade = input('Digite o nome da cidade que nasceu: ')
idade = int(input('Digite a sua idade: '))

if idade < 18:
    print(f'\n{nome}, você é menor de idade, não poderá seguir com o processo.')
else:
    print(f'\n{nome}, você é maior de idade é poderá procurar a agência mais próxima da cidade de {cidade}.')