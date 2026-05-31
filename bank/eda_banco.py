import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ruta = r"C:\Users\HLSG53257343\OneDrive - Bamesa Aceros\Formación\DataAnalytics\Proyecto4_Python for data\EDA\bank-additional.csv"

df = pd.read_csv(ruta)

print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.describe())
df = df.drop("Unnamed: 0", axis=1)

print(df.columns)
print(df.select_dtypes(include=["object", "string"]).columns)
print(df.dtypes)
columnas_numericas = [
    "cons.price.idx",
    "cons.conf.idx",
    "euribor3m",
    "nr.employed"
]

for col in columnas_numericas:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print(df.dtypes)
print(df["y"].value_counts())
print(df["y"].value_counts(normalize=True) * 100)
print(df["job"].value_counts())
print(pd.crosstab(df["job"], df["y"]))
conversion_job = pd.crosstab(df["job"], df["y"], normalize="index") * 100

print(conversion_job)
conversion_job["yes"].sort_values().plot(kind="barh")

plt.title("Conversion por profesion")
plt.xlabel("Porcentaje de yes")
plt.ylabel("Profesion")

plt.show()
plt.figure(figsize=(10,5))

df.boxplot(column="age", by="y")

plt.title("Edad por conversion")
plt.suptitle("")

plt.ylabel("Edad")

plt.show()
bins = [0, 30, 40, 50, 60, 100]

labels = [
    "0-30",
    "31-40",
    "41-50",
    "51-60",
    "60+"
]

df["grupo_edad"] = pd.cut(df["age"], bins=bins, labels=labels)

print(df["grupo_edad"].value_counts())
conversion_edad = pd.crosstab(
    df["grupo_edad"],
    df["y"],
    normalize="index"
) * 100

print(conversion_edad)
conversion_edad["yes"].plot(kind="bar")

plt.title("Conversion por grupo de edad")
plt.xlabel("Grupo de edad")
plt.ylabel("Porcentaje de yes")

plt.show()

df.to_csv(
    r"C:\Users\HLSG53257343\OneDrive - Bamesa Aceros\Formación\DataAnalytics\Proyecto4_Python for data\EDA\bank_limpio.csv",
    index=False
)

print("Archivo exportado correctamente")