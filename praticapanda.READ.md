O que está acontecendo?

import pandas as pd

— Você está importando a biblioteca Pandas, que é usada para trabalhar com tabelas e dados estruturados.

Criando um dicionário chamado dados

— Cada chave ("Nome", "Idade", "Cidade") vira uma coluna.
— Cada lista associada vira os valores dessa coluna.

Transformando o dicionário em DataFrame
git
— df = pd.DataFrame(dados) cria uma tabela com essas colunas e dados.

Filtrando pessoas com idade maior que 30

— df["Idade"] > 30 cria uma condição booleana.
— df[df["Idade"] > 30] retorna só as linhas onde essa condição é verdadeira. 

O que está acontecendo?

import pandas as pd

— Você está importando a biblioteca Pandas, que é usada para trabalhar com tabelas e dados estruturados.

Criando um dicionário chamado dados

— Cada chave ("Nome", "Idade", "Cidade") vira uma coluna.
— Cada lista associada vira os valores dessa coluna.

Transformando o dicionário em DataFrame
— df = pd.DataFrame(dados) cria uma tabela com essas colunas e dados.

Filtrando pessoas com idade maior que 30
— df["Idade"] > 30 cria uma condição booleana.
— df[df["Idade"] > 30] retorna só as linhas onde essa condição é verdadeira.


Resultado exibido:

Ele vai mostrar Bruno e Carlos, porque têm idade acima de 30.