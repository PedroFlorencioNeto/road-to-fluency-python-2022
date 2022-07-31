# ------------------------------------------------------------------------------------ #

# Paradigma da Programação Funcional em Python

# Por: Pedro Florencio de Almeida Neto - pedroflorencio@alu.ufc.br

# ------------------------------------------------------------------------------------ #

# ------------------------------------------------------------------------------------ #

# Você foi chamado para trabalhar como novo programador Python para o aplicativo Spotify, analisando as avaliações de músicas pelos usuários. 

# O seu chefe está muito entusiasmado com a sua chegada e já pensou em várias perguntas para você responder. 

# Ele coletou diversas avaliações dos gêneros musicais Rock e Pop.

# Em cada avaliação o usuário pode dar uma nota em quantidade de estrelas para uma música, de 1 a 5. 

# Ele quer que você mapeie as avaliações numéricas em categorias: 

# Entre 0 e 1 estrelas é uma música ruim, entre 2 e 3 é uma música mediana e entre 4 e 5 são para as músicas boas. 

# O seu papel é dizer para o seu chefe quantas músicas ruins, medianas e boas existem para cada gênero: Rock e Pop.

# Além disso, ele quer saber se existe alguma música mediana de Rock e se todas as músicas de Pop são boas. 

# Por fim, quer saber qual gênero musical teve uma maior quantidade de músicas boas. Abaixo seguem as notas de cada gênero.

# notas_rock = [5, 1, 4, 0, 2, 5, 2, 1, 0, 5, 5, 3, 5, 2, 5, 5, 3, 5, 4, 4]
# notas_pop = [3, 2, 5, 1, 2, 1, 4, 1, 5, 0, 4, 2, 1, 2, 5, 2, 4, 4, 0, 1]

# Pronto, com essas informações você pode começar a desenvolver um programa em Python capaz de responder as perguntas do seu chefe.

# ------------------------------------------------------------------------------------ #

# 1. Quantas músicas ruins, medianas e boas existem para cada gênero (Rock e Pop)?

notas_rock = [5, 1, 4, 0, 2, 5, 2, 1, 0, 5, 5, 3, 5, 2, 5, 5, 3, 5, 4, 4]
notas_pop = [3, 2, 5, 1, 2, 1, 4, 1, 5, 0, 4, 2, 1, 2, 5, 2, 4, 4, 0, 1]

# Função de categoriza as notas das músicas

# Ruins: 0 a 1
# Medianas: 2 a 3
# Boas: 4 a 5

def categoria(nota):
    if nota < 2:
        return 'ruim'
    elif nota > 1 and nota < 4:
        return 'mediana'
    else:
        return 'boa'

# Aplicação da função de categorização na lista de notas de cada gênero
classificacao_rock = list(map(categoria,notas_rock))
classificacao_pop = list(map(categoria,notas_pop))

# Quantidade de notas ruins para cada gênero
qtde_ruins_rock = len(list(filter(lambda x:x=='ruim',classificacao_rock)))
qtde_ruins_pop = len(list(filter(lambda x:x=='ruim',classificacao_pop)))

# Quantidade de notas medianas para cada gênero
qtde_medianas_rock = len(list(filter(lambda x:x=='mediana',classificacao_rock)))
qtde_medianas_pop = len(list(filter(lambda x:x=='mediana',classificacao_pop)))

# Quantidade de notas boas para cada gênero
qtde_boas_rock = len(list(filter(lambda x:x=='boa',classificacao_rock)))
qtde_boas_pop = len(list(filter(lambda x:x=='boa',classificacao_pop)))

print('\nQuestão 1\nRock: {} ruins, {} medianas e {} boas. Pop: {} ruins, {} medianas e {} boas.'.format(
    qtde_ruins_rock, qtde_medianas_rock, qtde_boas_rock,
    qtde_ruins_pop, qtde_medianas_pop, qtde_boas_pop
))

# ------------------------------------------------------------------------------------ #

# 2. Existe alguma música mediana de Rock?

print('\nQuestão 2\nExiste música mediana de Rock? {}'.format(any(list(filter(lambda x:x=='mediana',classificacao_rock)))))

# ------------------------------------------------------------------------------------ #

# 3. Qual gênero musical teve uma maior quantidade de músicas boas?

if qtde_boas_pop > qtde_boas_rock: print('\nQuestão 3\n Tem mais músicas boas de Rock\n')
else: print('\nQuestão 3\n Tem mais músicas boas de Rock\n')

# ------------------------------------------------------------------------------------ #