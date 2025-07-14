import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns

df = pd.read_csv("dataset_vivienda.csv")

df["precio_metro"] = df["precio"] / df["area"]

df = df.dropna(subset=["descripcion"])

plt.figure(figsize=(12, 6))

sns.scatterplot(data=df, x="precio", y="precio_metro", hue="descripcion", alpha=0.7)

plt.title("Relación entre precio y precio por metro cuadrado por tipo de vivienda")
plt.xlabel("Precio total (COP)")
plt.ylabel("Precio por metro cuadrado (COP)")
plt.gca().xaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'{int(x/1e6)}M'))
plt.gca().xaxis.set_major_locator(mtick.MultipleLocator(50_000_000))
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

plt.show()
