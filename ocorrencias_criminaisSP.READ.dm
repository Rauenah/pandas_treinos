#  Análise de Ocorrências Criminais com KMeans

Este projeto analisa dados de ocorrências criminais mensais do Estado de São Paulo e aplica a técnica de KMeans clustering  para identificar padrões semelhantes entre diferentes tipos de crimes.

---

## O que é KMeans?

O **KMeans** é um algoritmo de agrupamento (clustering).  
Ele pega os dados e tenta dividir em grupos (clusters) de forma que os elementos dentro de cada grupo sejam **parecidos entre si**.

 Importante: aqui o agrupamento é **estatístico**, não jurídico.  
Ou seja, o algoritmo não sabe o que é “hediondo” ou “leve”. Ele apenas olha para os números mensais e junta crimes que variam de forma semelhante.

---

## Passo a passo do código

1. **Carregar os dados**  
   Lemos o arquivo Excel com os crimes e suas ocorrências mensais.

2. **Garantir que os meses sejam números**  
   Transformamos colunas como “Janeiro”, “Fevereiro” etc. em valores numéricos.  
   Se houver texto estranho, ele vira `NaN`.

3. **Renomear colunas para abreviações**  
   Para facilitar, renomeamos “Janeiro” → “Jan”, “Fevereiro” → “Fev”, etc.

4. **Selecionar apenas os meses (Jan–Dez)**  
   Pegamos apenas os números mensais, ignorando a coluna “Total”.

5. **Normalizar os dados**  
   Crimes diferentes têm escalas diferentes (ex.: homicídios são centenas, furtos são milhares).  
   Normalizar coloca tudo na mesma base para comparar.

6. **Aplicar KMeans**  
   O algoritmo cria 3 grupos (clusters) e diz em qual grupo cada crime entrou.

7. **Visualizar os clusters**  
   Em vez de mostrar todas as linhas (que fica confuso), mostramos **apenas a média de cada cluster**.  
   Assim dá para ver claramente os padrões.

---

## Resultado

O gráfico gerado mostra a **média mensal de ocorrências por cluster**:

![Clusters de crimes](clusters.png)

- **Cluster 0**: crimes com valores altos e padrão parecido (ex.: furtos e roubos).  
- **Cluster 1**: crimes com valores médios e comportamento mais estável.  
- **Cluster 2**: crimes raros ou com números baixos, mas que ainda seguem um padrão próprio.  

---

## Como salvar o gráfico

No código, adicione:

```python
plt.savefig("clusters.png")


#Este projeto mostra como usar ciência de dados para encontrar padrões em estatísticas criminais.
Mesmo sem entender de leis ou categorias jurídicas, 
o algoritmo ajuda a identificar comportamentos semelhantes entre diferentes tipos de crimes ao longo do ano.

xlsx tirada do Portal de SSP-SP https://www.ssp.sp.gov.br/estatistica/dados-mensais
