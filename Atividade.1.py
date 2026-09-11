"""
Atividade 1 - Métricas de Regressão
Dataset: California Housing

Observação sobre o carregamento dos dados:
Em ambientes com acesso normal à internet, o dataset é carregado com:

    from sklearn.datasets import fetch_california_housing
    dados = fetch_california_housing(as_frame=True)
    df = dados.frame

Neste ambiente de execução o domínio usado pelo scikit-learn para baixar o
arquivo (ndownloader.figshare.com) está bloqueado, então os mesmos dados
(StatLib California Housing, usados pelo próprio scikit-learn) foram obtidos
de um espelho CSV e transformados exatamente nas colunas que o
fetch_california_housing produz (MedInc, HouseAge, AveRooms, AveBedrms,
Population, AveOccup, Latitude, Longitude, MedHouseVal). O conteúdo final é
idêntico ao que o código acima geraria.
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

pd.set_option("display.width", 120)

# ---------------------------------------------------------------
# Carregamento (equivalente a fetch_california_housing(as_frame=True))
# ---------------------------------------------------------------
url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"
raw = pd.read_csv(url)

df = pd.DataFrame({
    "MedInc": raw["median_income"],
    "HouseAge": raw["housing_median_age"],
    "AveRooms": raw["total_rooms"] / raw["households"],
    "AveBedrms": raw["total_bedrooms"] / raw["households"],
    "Population": raw["population"],
    "AveOccup": raw["population"] / raw["households"],
    "Latitude": raw["latitude"],
    "Longitude": raw["longitude"],
    "MedHouseVal": raw["median_house_value"] / 100000.0,
})

print("="*70)
print("1) Atributos (colunas) do dataset")
print("="*70)
print(list(df.columns))

print("\n" + "="*70)
print("2) Número de linhas (bairros)")
print("="*70)
print(df.shape[0], "linhas,", df.shape[1], "colunas")

print("\n" + "="*70)
print("4) Valores ausentes")
print("="*70)
print(df.isnull().sum())
print("Total de valores ausentes:", df.isnull().sum().sum())

# ---------------------------------------------------------------
# 6) Escolha do atributo - correlação com o alvo
# ---------------------------------------------------------------
print("\n" + "="*70)
print("Correlação de cada atributo com MedHouseVal (para embasar a escolha)")
print("="*70)
corr = df.corr(numeric_only=True)["MedHouseVal"].sort_values(ascending=False)
print(corr)

x_col = "MedInc"  # maior correlação absoluta com o alvo

# ---------------------------------------------------------------
# 7) Gráfico de dispersão
# ---------------------------------------------------------------
plt.figure(figsize=(7, 5))
plt.scatter(df[x_col], df["MedHouseVal"], alpha=0.15, s=10, color="#2563eb")
plt.xlabel(x_col + " (renda média, em dezenas de milhares de USD)")
plt.ylabel("MedHouseVal (valor médio da casa, em centenas de milhares de USD)")
plt.title(f"{x_col} vs MedHouseVal")
plt.tight_layout()
plt.savefig("scatter_medinc.png", dpi=130)
plt.close()

# ---------------------------------------------------------------
# 8) Split treino/teste
# ---------------------------------------------------------------
X = df[[x_col]]
y = df["MedHouseVal"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("\n" + "="*70)
print("8) Tamanho dos conjuntos")
print("="*70)
print("Treino:", X_train.shape[0], "| Teste:", X_test.shape[0])

# ---------------------------------------------------------------
# 9-11) Treino do modelo e métricas
# ---------------------------------------------------------------
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n" + "="*70)
print(f"10) Modelo treinado com x = {x_col}")
print("="*70)
print("Coeficiente (coef_):", model.coef_[0])
print("Intercepto (intercept_):", model.intercept_)

print("\n" + "="*70)
print("11) Métricas no conjunto de teste")
print("="*70)
print("MSE:", mse)
print("RMSE:", np.sqrt(mse))
print("R²:", r2)

# ---------------------------------------------------------------
# 13) Desafio bônus - trocar o atributo
# ---------------------------------------------------------------
x_col2 = "AveRooms"
X2 = df[[x_col2]]
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y, test_size=0.2, random_state=42)
model2 = LinearRegression()
model2.fit(X2_train, y2_train)
y2_pred = model2.predict(X2_test)
mse2 = mean_squared_error(y2_test, y2_pred)
r2_2 = r2_score(y2_test, y2_pred)

print("\n" + "="*70)
print(f"13) Bônus - modelo alternativo com x = {x_col2}")
print("="*70)
print("Coeficiente:", model2.coef_[0])
print("Intercepto:", model2.intercept_)
print("MSE:", mse2)
print("R²:", r2_2)

print("\nComparação:")
print(f"  {x_col}:  R² = {r2:.4f}")
print(f"  {x_col2}: R² = {r2_2:.4f}")