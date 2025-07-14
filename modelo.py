import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv("dataset_vivienda.csv")






X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
