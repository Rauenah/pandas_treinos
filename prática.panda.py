import pandas as pd

#CRIANDO  UMA DATAFRAME

dados = {
     "Nome": ["Ana", "Bruno", "Carlos"],
     "Idade": [23,35,42],
     "Cidade":["São Paulo", "Rio de Janeiro", "Minas Gerais"]

}
df = pd.DataFrame(dados)

#FILTRAR PESSOAS COM IDADE MAIOR QUE 30

print(df[df["Idade"] > 30])
