import pandas as pd
from tabulate import tabulate

df = pd.read_csv('dataset_vivienda.csv')

total_viviendas = len(df)

df['precio_metro'] = df['precio'] / df['area']
precio_metro = round(df['precio_metro'].mean())

resumen = df['descripcion'].value_counts().reset_index()
resumen.columns = ['Tipo de vivienda', 'Cantidad']

print("Estadisticas:")
print("")
print(tabulate([[total_viviendas, precio_metro]], 
               headers=["Cantidad de viviendas", 
                        "Promedio del precio por metro cuadrado"], 
               tablefmt='fancy_grid'))
print("")

print("Clasificación por tipo de vivienda:")
print("")
print(tabulate(resumen, 
               headers='keys', 
               tablefmt='fancy_grid', 
               showindex=False))