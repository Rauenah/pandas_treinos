#Esse script:

#Usa Pandas para organizar os dados,
#Divide em treino/teste,
#Treina um modelo de regressão logística,
#E imprime a acurácia final.

#Acurácia é uma medida de desempenho que mostra a proporção de previsões corretas feitas 
#por um modelo em relação ao total de casos avaliados.
#Ou seja, indica quantos resultados o modelo acertou dentro de todas as tentativas.


import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


# Carregar dataset e transformar em DataFrame

iris = load_iris ()
df= pd.DataFrame(iris.data, columns= iris.feature_names)
df['species'] = iris.target

# Separar treino/teste e treinar modelo

X_train, X_test, y_train, y_test = train_test_split(df[iris.feature_names], df['species'], test_size=0.2)
print("Acurácia:", LogisticRegression(max_iter=200).fit(X_train, y_train).score(X_test, y_test))
