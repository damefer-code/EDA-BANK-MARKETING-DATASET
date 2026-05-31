import pandas as pd

ruta = r"C:\Users\HLSG53257343\OneDrive - Bamesa Aceros\Formación\DataAnalytics\Proyecto4_Python for data\EDA\customer-details.xlsx"

excel = pd.ExcelFile(ruta)

print("Hojas encontradas:")
print(excel.sheet_names)

df = pd.concat(
    [pd.read_excel(ruta, sheet_name=hoja) for hoja in excel.sheet_names],
    ignore_index=True
)

print("\nPrimeras filas:")
print(df.head())

print("\nInformación:")
print(df.info())

print("\nValores nulos:")
print(df.isnull().sum())

print("\nDuplicados:")
print(df.duplicated().sum())

print("\nEstadísticas:")
print(df.describe())

df.drop(columns=["Unnamed: 0"], inplace=True)

print("\nValores nulos:")
print(df.isnull().sum())

print("\nDuplicados:")
print(df.duplicated().sum())

print("\nCorrelaciones:")
print(df.select_dtypes(include="number").corr())


import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.hist(df["Income"], bins=30)
plt.title("Distribución de ingresos")
plt.xlabel("Income")
plt.ylabel("Clientes")
plt.show()

plt.figure(figsize=(8,5))
df["Kidhome"].value_counts().sort_index().plot(kind="bar")
plt.title("Número de hijos por hogar")
plt.xlabel("Kidhome")
plt.ylabel("Clientes")
plt.show()

plt.figure(figsize=(10,6))
plt.boxplot(df["NumWebVisitsMonth"])
plt.title("Visitas web mensuales")
plt.ylabel("Visitas")
plt.show()

plt.figure(figsize=(10,5))
plt.boxplot(df["Income"])
plt.title("Boxplot de ingresos")
plt.ylabel("Income (€)")
plt.show()

print(df["NumWebVisitsMonth"].value_counts().sort_index())

import seaborn as sns
import matplotlib.pyplot as plt

corr = df.select_dtypes(include='number').corr()

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Matriz de correlación')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

corr = df.select_dtypes(include="number").corr()

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Matriz de correlación")
plt.show()