import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv("dataset_vivienda.csv")

anio = datetime.now().year

df.dropna(subset=['descripcion', 'precio', 'area'], inplace=True)

df.rename(columns={'descripcion': 'tipo_de_vivienda'}, inplace=True)

df['anio_construccion'] = anio - df['antiguedad']

df.drop('antiguedad', axis=1, inplace=True)

X_numericos = df[['precio', 'area', 'habitaciones', 'anio_construccion']]

encoder = OneHotEncoder(drop='first', sparse_output=False)
X_categoricas = encoder.fit_transform(df[['tipo_de_vivienda']])

X = np.concatenate([X_numericos.values, X_categoricas], axis=1)

y = df['precio']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

print("Intercepto:", modelo.intercept_)
print("Coeficientes:", modelo.coef_)


y_pred = modelo.predict(X_test)

plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.xlabel("Precio real")
plt.ylabel("Precio predicho")
plt.title("Regresión lineal: Precio real vs predicho")
plt.grid(True)
plt.tight_layout()
plt.show()
y_pred = modelo.predict(X_test)

plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.xlabel("Precio real")
plt.ylabel("Precio predicho")
plt.title("Regresión lineal: Precio real vs predicho")
plt.grid(True)
plt.tight_layout()
plt.show()
