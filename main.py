import pandas as pd

df = pd.read_csv('dataset_vivienda.csv')

print(df.head())



import matplotlib.pyplot as plt 
from datetime import datetime
anio = datetime.now().year

df['anio_construccion'] = anio - df['antiguedad'] 

df.drop('antiguedad', axis=1, inplace=True)

df.rename(columns={'descripcion': 'tipo_de_vivienda'}, inplace=True)

#print(df.head())

#print(df.describe())

#print(df.dtypes)
#unicos = df['descripcion'].unique()


#print(df['descripcion'].value_counts())
#print(df.isnull().mean() * 100)
#print(df['tipo_de_vivienda'].unique())
#df.plot()
