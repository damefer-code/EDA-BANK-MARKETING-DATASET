import pandas as pd

# -----------------------------
# CARGA DATASET BANK
# -----------------------------
ruta_bank = r"C:\Users\HLSG53257343\OneDrive - Bamesa Aceros\Formación\DataAnalytics\Proyecto4_Python for data\EDA\bank-additional.csv"

df_bank = pd.read_csv(ruta_bank)

print("BANK")
print(df_bank.shape)
print(df_bank.columns)

# -----------------------------
# CARGA DATASET CUSTOMER
# -----------------------------
ruta_customer = r"C:\Users\HLSG53257343\OneDrive - Bamesa Aceros\Formación\DataAnalytics\Proyecto4_Python for data\EDA\customer-details.xlsx"

excel = pd.ExcelFile(ruta_customer)

df_customer = pd.concat(
    [pd.read_excel(ruta_customer, sheet_name=hoja)
     for hoja in excel.sheet_names],
    ignore_index=True
)

# Limpieza
if "Unnamed: 0" in df_customer.columns:
    df_customer.drop(columns=["Unnamed: 0"], inplace=True)

# Renombrar ID para que coincida
df_customer.rename(columns={"ID": "id_"}, inplace=True)

print("\nCUSTOMER")
print(df_customer.shape)
print(df_customer.columns)

# -----------------------------
# COMPROBAR IDS
# -----------------------------
print("\nCoincidencias de ID")

ids_bank = set(df_bank["id_"])
ids_customer = set(df_customer["id_"])

coinciden = len(ids_bank.intersection(ids_customer))

print(f"IDs bank: {len(ids_bank)}")
print(f"IDs customer: {len(ids_customer)}")
print(f"IDs coincidentes: {coinciden}")


df_merge = df_bank.merge(df_customer, on="id_", how="left")

print("\nDATASET CRUZADO")
print(df_merge.shape)
print(df_merge.head())
print(df_merge.isnull().sum())

df_merge.to_csv(
    r"C:\Users\HLSG53257343\OneDrive - Bamesa Aceros\Formación\DataAnalytics\Proyecto4_Python for data\EDA\bank_customer_merge.csv",
    index=False
)

print("\nIngreso medio según contratación:")
print(df_merge.groupby("y")["Income"].mean())

print("\nVisitas web medias según contratación:")
print(df_merge.groupby("y")["NumWebVisitsMonth"].mean())


print("\nContratación por hijos:")
print(pd.crosstab(df_merge["Kidhome"], df_merge["y"], normalize="index") * 100)

print("\nContratación por adolescentes:")
print(pd.crosstab(df_merge["Teenhome"], df_merge["y"], normalize="index") * 100)

import pandas as pd
import matplotlib.pyplot as plt

contratacion_hijos = (
    pd.crosstab(df_merge["Kidhome"], df_merge["y"], normalize="index") * 100
)

plt.figure(figsize=(8,5))
contratacion_hijos["yes"].plot(kind="bar")

plt.title("Tasa de contratación según número de hijos")
plt.xlabel("Número de hijos")
plt.ylabel("% clientes que contrataron")
plt.xticks(rotation=0)

plt.show()

income_medio = df_merge.groupby("y")["Income"].mean()

plt.figure(figsize=(8,5))
income_medio.plot(kind="bar")

plt.title("Ingreso medio según contratación")
plt.xlabel("Contrató depósito")
plt.ylabel("Ingreso medio (€)")
plt.xticks(rotation=0)

plt.show()

ax = income_medio.plot(kind="bar", figsize=(8,5))

for p in ax.patches:
    ax.annotate(
        f"{p.get_height():,.0f}",
        (p.get_x() + p.get_width()/2, p.get_height()),
        ha="center",
        va="bottom"
    )

plt.title("Ingreso medio según contratación")
plt.ylabel("Ingreso medio (€)")
plt.xticks(rotation=0)

plt.show()