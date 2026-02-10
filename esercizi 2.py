import pandas as pd
import numpy as np

# data = {
#     "Altezza_cm":[170,165,180,175],
#     "Peso_kg":[65,70,80,75]
# }
# df = pd.DataFrame(data)
# df["BMI"] = df["Peso_kg"] / (df["Altezza_cm"] / 100 ) ** 2

# data = {
#     "Colore":["Rosso","Blue","Verde","Rosso"],
#     "Prezzo":[10,20,15,30]
# }
# df = pd.DataFrame(data)
# df_encoded = pd.get_dummies(df,columns=["Colore"])
# print(df_encoded)

# data = {
#     "Data": pd.to_datetime(["2023-01-01","2023-02-15","2023-03-20"]),
#     "Vendite":[100,150,200]
# }
#
# df = pd.DataFrame(data)
#
# df["Mese"] = df["Data"].dt.month
# df["Vendite_log"] = df["Vendite"].apply(lambda x: np.log1p(x))
# df["Mese*Vendite"] = df["Mese"] * df["Vendite"]
#
# print(df)
# Esercizio 1
# data = {
#     "Lunghezza":[20,4,6,9,12],
#     "Larghezza":[3,10,34,8,6]
# }
# df = pd.DataFrame(data)
#
# df["Area_Rettangolo"] = df["Lunghezza"] * df["Larghezza"]
# print(df)

# Esercizio 2
# data = {
#     "Tipo":["A","B","C","D"],
#     "Valore":[10,20,34,45]
# }
#
# df = pd.DataFrame(data)
# df_encoded = pd.get_dummies(df,columns=["Tipo"])
# print(df_encoded)
# Esercizio 3
data = {
    "Data":pd.date_range(start="2026-01-01",end="2026-01-10",freq="D"),
    "Valori":np.random.randint(30,200,size=10)
}
df = pd.DataFrame(data)
df["Giorno_Settimana"] = df["Data"].dt.day_name()
df["Mese"] = df["Data"].dt.month
df["Diff_prec"] = df["Valori"].diff()
df["Interazione_mese_valore"] = df["Mese"] * df["Valori"]
print(df)

# df = pd.DataFrame({
#     "id": np.arange(1,1000001),
#     "prezzo": np.random.uniform(1,100,1000000)
# })
#
# print(df.memory_usage(deep=True).sum() / 1024 ** 2)
#
# df["id"] = pd.to_numeric(df["id"],downcast="integer")
# df["prezzo"] = pd.to_numeric(df["prezzo"],downcast="float")
#
# print(df.memory_usage(deep=True).sum() / 1024 ** 2)

# df = pd.DataFrame({
#     "categorie": np.random.choice(["A","B","C","D"] , size=1000000)
# })
# print(df.memory_usage(deep=True).sum() / 1024 ** 2)
#
# df["categorie"] = df["categorie"].astype("category")
# print(df.memory_usage(deep=True).sum() / 1024 ** 2)

# df = pd.DataFrame({
#     "user_id":np.random.randint(1,200001,1000000),
#     "product_category": np.random.choice(["elettronica","abbigliamento","giocatoli","libri"],size=1000000),
#     "purchase_amount": np.random.uniform(5,500,1000000),
#     "purchase_date":pd.date_range("2020-01-01",periods=1000000,freq="min").astype("str")
# })
# print(df.memory_usage(deep=True).sum() / 1024 ** 2)
#
# df["user_id"] = pd.to_numeric(df["user_id"],downcast="integer")
# df["product_category"] = df["product_category"].astype("category")
# df["purchase_amount"] = pd.to_numeric(df["purchase_amount"],downcast="float")
# df["purchase_date"] = pd.to_datetime(df["purchase_date"])
# print(df.memory_usage(deep=True).sum() / 1024 ** 2)

# Esercizio 1 Downcasting di int64 e float64
# df = pd.DataFrame({
#     "Interi":np.random.randint(1,1000000,size=1000000),
#     "Decimali":np.random.rand(1_000_000) * 1000
# })
#
# print("Info iniziale:\n")
# print(df.info(memory_usage="deep"))
# # Downcasting
# memoria_iniziale = df.memory_usage(deep=True).sum() // 1024 ** 2
#
# df["Interi"] = pd.to_numeric(df["Interi"],downcast="unsigned")
# df["Decimali"] = pd.to_numeric(df["Decimali"],downcast="float")

# memoria_finale = df.memory_usage(deep=True).sum() // 1024 ** 2
#
# print("Info dopo il downcasting:\n")
# print(df.info(memory_usage="deep"))
#
# print(f"Memoria iniziale: {memoria_iniziale:.2f} MB")
# print(f"Memoria finale: {memoria_finale:.2f} MB")
# print(f"Riduzione totale: {(memoria_iniziale - memoria_finale):.2f} MB")


# df = pd.DataFrame({"Citta":np.random.choice(["Roma","Milano","Firenze","Torino","Napoli"],size=1000000)})
# print("Prima della conversione:\n")
# print(df.info(memory_usage="deep"))
# memoria_iniziale = df.memory_usage(deep=True).sum() // 1024 ** 2
# df["Citta"] = df["Citta"].astype("category")
# print("Dopo la conversione: \n")
# print(df.info(memory_usage="deep"))
# memoria_finale = df.memory_usage(deep=True).sum() // 1024 ** 2
# print(f"Memoria iniziale: {memoria_iniziale:.2f} MB")
# print(f"Memoria finale: {memoria_finale:.2f} MB")
# print(f"Riduzione totale: {(memoria_iniziale - memoria_finale):.2f} MB")

# df = pd.DataFrame({
#     "id": np.random.randint(1,2_00_000,size=1_000_000),
#     "citta":np.random.choice(["Roma","Milano","Napoli","Torino","Firenze"],size=1_000_000),
#     "decimali":np.random.rand(1_000_000) * 1000,
#     "data": pd.date_range("2022-01-01",freq="min",periods=1_000_000)
# })
#
# print("Info del DF prima della downcasting: \n")
# print(df.info(memory_usage="deep"))
# memoria_iniziale = df.memory_usage(deep=True).sum() // 1024 ** 2
#
# df["id"] = pd.to_numeric(df["id"],downcast="integer")
# df["citta"] = df["citta"].astype("category")
# df["decimali"] = pd.to_numeric(df["decimali"],downcast="float")
# df["data"] = pd.to_datetime(df["data"])
# memoria_finale = df.memory_usage(deep=True).sum() // 1024 ** 2
# print("Info del DF dopo il downcasting: \n")
# print(df.info(memory_usage="deep"))
# print(f"Memoria iniziale: {memoria_iniziale:.2f} MB")
# print(f"Memoria finale: {memoria_finale:.2f} MB")
# print(f"Riduzione totale: {(memoria_iniziale - memoria_finale):.2f} MB")
# print("Scelta ottimale per ridurre il carico della memoria")