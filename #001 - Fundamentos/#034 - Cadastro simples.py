'''
Você precisa criar um pequeno programa para registrar informações básicas de um usuário.

Requisitos do programa:
1. Criar variáveis para:
    Nome do usuário (str)
    Idade (int)
    Altura (float)
    Usuário ativo (bool)
2. Exibir todas as informações na tela usando print() e f-strings
3. Usar comentários para explicar o código
4. Mostrar os dados de forma organizada (uma informação por linha)

📌 Conteúdo avaliado:
1. Variáveis
2. Tipos de dados
3. print()
4. f-strings
5. Comentários
'''
# Ficha Cadastral do Aluno
nome_aluno = "Bernadette Louise Silva"
idade = 33
altura = 1.71
situacao_cad = True

# Dados em tela
print(f'Infomações do Aluno(a):\n'
      f'Nome....: {nome_aluno}\n'
      f'Idade...: {idade}\n'
      f'Altura..: {altura}\n'
      f'Situação: {situacao_cad}\n'
      )

# Fim do código