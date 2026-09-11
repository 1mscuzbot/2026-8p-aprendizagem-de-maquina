# BIBLIOTECAS UTILIZADAS
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_teste_split


# DEIXA OS GRÁFICOS COM UM TAMANHO MAIS CONFORTÁVEL
plt.rcParams["figure.figsize"] = (7, 4.5)



np.random.seed(42)

tamanho = np.random.uniform(30, 200, 150)  			# m²
preco = 3000* tamanho + np.random.normal(0, 20000, 150) + 50000 #

df = pd.DataFrame({"tamanho_m2": tamanho, "preco": preco})
df.to_csv("imoveis.csv", index=False)

df.head()