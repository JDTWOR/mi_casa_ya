from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('dataset_vivienda.csv')

anio = datetime.now().year

df['anio_construccion'] = anio - df['antiguedad'] 

df.drop('antiguedad', axis=1, inplace=True)

#print(df.isnull().sum())

#print(df.isnull().mean() * 100)
print(df.head())
#df.plot()
#plt.show()
