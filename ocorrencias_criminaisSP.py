import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Carregar arquivo xlsx
df = pd.read_excel("OcorrenciaMensal(Criminal)-EstadoSP_20260106_221847.xlsx")

# Converter colunas de meses para numérico
meses_extenso = ["Janeiro","Fevereiro","Marco","Abril","Maio","Junho",
                 "Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

for col in meses_extenso:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Renomear colunas para abreviações
df.rename(columns={
    "Janeiro":"Jan", "Fevereiro":"Fev", "Marco":"Mar",
    "Abril":"Abr", "Maio":"Mai", "Junho":"Jun",
    "Julho":"Jul", "Agosto":"Ago", "Setembro":"Set",
    "Outubro":"Out", "Novembro":"Nov", "Dezembro":"Dez"
}, inplace=True)

# Selecionar apenas colunas de meses (Jan-Dez)
meses = ["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]
X = df[meses].fillna(0)   # Preencher NaN com 0

# Normalizar os dados
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Aplicar KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
df["Cluster"] = kmeans.fit_predict(X_scaled)

# Ver quais crimes caíram em cada cluster
print(df[["Natureza", "Cluster"]])

# Visualizar os clusters

plt.figure(figsize=(10,6))
for cluster in sorted(df["Cluster"].unique()):
    media = df[df["Cluster"] == cluster][meses].mean()
    plt.plot(meses, media, marker='o', label=f"Cluster {cluster}")
    
plt.title("Média mensal de ocorrências criminais por cluster")
plt.xlabel("Meses")
plt.ylabel("Ocorrências médias")
plt.legend()
plt.grid(True)
plt.show()

# Salvar o gráfico como imagem
plt.savefig("clusters.png")

# Mostrar na tela
plt.show()










