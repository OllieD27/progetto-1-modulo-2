import pandas as pd
import numpy as np
import hashlib
import matplotlib.pyplot as plt
import time
from sklearn.impute import KNNImputer
# from sklearn.impute import IterativeImputer
# from sklearn.experimental import enable_iterative_imputer
from sklearn.ensemble import IsolationForest
from datetime import date,datetime

# Esercizio Pandas

# dati = {"Settimana":[1,2,3,4,5,6],
#         "Vendite":[230,400,323,454,494,223]
#         }
#
# df = pd.DataFrame(dati)
# # Valore Medio, Massimo,Il valore massimo di una settimana.
#
# media_vendite = df["Vendite"].mean()
# massimo = df["Vendite"].max()
# settimana = df.loc[df["Vendite"].idxmax()]
# print(settimana["Settimana"])
# print(f"Giorno con vendite massime: {massimo}")
# print(f"Media vendite: {media_vendite}")
#
# # Rappresentazione di un Grafico a Barre
# plt.bar(df["Settimana"],df["Vendite"],color="skyblue")
# plt.axhline(media_vendite,color="red",linestyle="--",label="Media")
# plt.xlabel("Settimana")
# plt.ylabel("Vendite")
# plt.title("Vendite Settimanali")
# plt.legend()
# plt.show()
#
# # Maschera per filtrare se un valore e sotto o sopra la media.
# mask_1 = df["Vendite"] > media_vendite
# mask_2 = df["Vendite"] < media_vendite
#
# # Doppio Grafico a Barre e Linea
# fig,ax = plt.subplots(2,1,figsize=(8,10))
# ax[0].bar(df["Settimana"][mask_1], df["Vendite"][mask_1],color="green")
# ax[0].bar(df["Settimana"][mask_2], df["Vendite"][mask_2],color="red")
# ax[0].set_title("Incasso per settimana")
# ax[1].plot(df["Settimana"],df["Vendite"],color="red")
# ax[1].set_title("Incasso per settimana")
# plt.tight_layout()
# plt.show()
# Esempio di un DF di Prezzi dove si aggiunge un'altra colonna con il prezzo scontato di 20%
# data = {"Prezzo":[100,200,300,400,500]}
# df = pd.DataFrame(data)
# df["Prezzo_Scontato"] = df["Prezzo"] * 0.8
#Esempio di aggiungere un'altra colonna dove si applica una maschera per classificare
# se un prezzo e piu alto o piu basso rispetto la media
# df["Categoria"] = np.where(df["Prezzo"] > 250,"Alto","Basso")
# print(df)
# Esempio di una operazioni vettoriali di due colonne
# data = {
#     "Prodotto":["A","B","C","D"],
#     "Quantita":[10,5,3,8],
#     "Prezzo_unitario":[20,50,15,30]
# }
# df = pd.DataFrame(data)
# df["Totale"] = df["Quantita"] * df["Prezzo_unitario"]
# print(df)
# Esercizio 1 df["Celsius"] + df["Fahrenheit"]
# temp = {
#     "Celsius":[23,12,10,4,2]
# }
# df = pd.DataFrame(temp)
# df["Fahrenheit"] = (df["Celsius"] * 9/5) + 32
# print(df)
# Aggiungere un df con condizioni con una comprehension Python e con np.where()
# punteggi = {"Punteggi":[20,29,30,31,17,14]}
# df = pd.DataFrame(punteggi)
# df["Risultati"] = ["Promosso" if x >= 18 else "Bocciato" for x in df["Punteggi"]]
# df["Result"] = np.where(df["Punteggi"] >=18,"Promosso","Bocciato")
# print(df)
# Aggiungere una Nuova colonna che calcola il salario settimanale se le ore lavorate sono sopra 40 e aggiungere 10%
# stipendio = {
#     "Ore_lavorate":[40,45,30,32,50,40],
#     "Paga_oraria":[12,12,12,10,12,11]
# }
# df = pd.DataFrame(stipendio)
# df["Salario_settimanale"] = np.where(df["Ore_lavorate"] > 40,(df["Ore_lavorate"] * df["Paga_oraria"]) * 1.1,df["Ore_lavorate"] * df["Paga_oraria"])
# print(df)

# Imputazione con Pandas con valore medio
# data = {
#     "Nome":["Anna","Luca","Marta","Paolo"],
#     "Eta":[23,None,29,35],
#     "Citta":["Roma","Milano",None,"Torino"]
# }
# df = pd.DataFrame(data)
#
# df["Eta"]= df["Eta"].fillna(df["Eta"].mean())
# df["Citta"]=df["Citta"].fillna("Sconosciuta")
# print(df)
# Imputazione con Pandas con il valore mediano
# data = {
#     "Redditto":[25000,32000,None,58000,None,45000]
# }
# df = pd.DataFrame(data)
# df["Redditto"] = df["Redditto"].fillna(df["Redditto"].median())
# Imputazione con KNNImputer
# data = {
#     "Altezza":[170,165,np.nan,180,175],
#     "Peso":[65,np.nan,70,80,75]
# }
# df = pd.DataFrame(data)
# imputer = KNNImputer(n_neighbors=2)
# df_impute = pd.DataFrame(imputer.fit_transform(df),columns=df.columns)
# print(df_impute)
# Esercizio 1
# data_1 = {"Voti":[2,5,4,3,np.nan,10,8,np.nan,4,np.nan]}
# df = pd.DataFrame(data_1)
# df["Voti"]= df["Voti"].fillna(0)
# print(df)
# Esercizio 2

# data_2 = {
#     "Altezza":[167,178,np.nan,190,np.nan,183,164],
#     "Peso":[65,82,57,np.nan,86,74,np.nan],
#     "Eta":[34,23,45,np.nan,33,26,np.nan]
# }
# df = pd.DataFrame(data_2)
# media = df["Altezza"].fillna(df["Altezza"].mean())
# mediana = df["Peso"].fillna(df["Peso"].median())
# moda = df["Eta"].mode()[0]
# df["Altezza"] =  df["Altezza"].fillna(media)
# df["Peso"] = df["Peso"].fillna(mediana)
# df["Eta"] = df["Eta"].fillna(moda)
# print(df)
# imputer = KNNImputer(n_neighbors=2)
# df_imputed = pd.DataFrame(imputer.fit_transform(df),columns=df.columns)
# print(df_imputed)
#
# # imputer = IterativeImputer(max_iter=10,random_state=42)
# df_imputed = pd.DataFrame(imputer.fit_transform(df),columns=df.columns)
# df["Eta"].hist(alpha=0.5,label="Originale",color="red")
#
# df_imputed["Eta"].hist(alpha=0.5,label="Imputata",color="blue")
# plt.legend()
# plt.show()
# Rilevamento e gestione outlier

# df = pd.DataFrame({"vendite":[100,105,110,500,115,120,600]})
# Q1 = df["vendite"].quantile(0.25)
# Q3 = df["vendite"].quantile(0.75)
# IQR = Q3 - Q1
# df["vendite_clean"] = df["vendite"].mask((df["vendite"] < (Q1 - 1.5 * IQR)) | (df["vendite"] > (Q3 + 1.5 * IQR)),df["vendite"].median())
# print(df)

# data = {"valori":[10,12,11,13,12,100]}
# df = pd.DataFrame(data)
# media = df["valori"].mean()
# dev_std = df["valori"].std()
# df["Outlier"] = (abs(df["valori"] - media) > 2 * dev_std )
# print(df)
#
# data = {"valori":[5,7,8,5,6,100,120]}
# df = pd.DataFrame(data)
# Q1 = df["valori"].quantile(0.25)
# Q3 = df["valori"].quantile(0.75)
# IQR = Q3 - Q1
#
# limite_basso = Q1 - 1.5 * IQR
# limite_alto = Q3 + 1.5 * IQR
# df["Outlier"] = (df["valori"] < limite_basso) | (df["valori"] > limite_alto)
# print(df)

# data = {"valori":[5,7,8,5,6,100,120]}
# df = pd.DataFrame(data)
#
# model = IsolationForest(contamination=0.2,random_state=42)
# df["outlier"] = model.fit_predict(df[["valori"]])
# print(df)

# df = pd.DataFrame({"valori":[3,4,5,6,8,4,3,20,5,7]})
# media = df["valori"].mean()
# dev_std = df["valori"].std()
# df["outlier"] = (abs(df["valori"] - media) > 2 * dev_std)
# print(df)
# df = pd.DataFrame({"valori":[10,20,23,12,21,23,14,13,23,19,35,89,65]})
# Q1 = df["valori"].quantile(0.25)
# Q3 = df["valori"].quantile(0.75)
# IQR = Q3 - Q1
# lower = Q1 - 1.5 * IQR
# upper = Q3 + 1.5 * IQR
# df["Outlier"] = ((df["valori"] < lower) | (df["valori"] > upper))
# print(df)

# data = {"Altezza":[175,166,130,155,189,204,199],"Peso":[66,57,43,89,110,67,73]}
# df = pd.DataFrame(data)
# model = IsolationForest(contamination=0.2,random_state=42)
# df["Outlier_Altezza"] = model.fit_predict(df[["Altezza"]])
# df["Outlier_Peso"] = model.fit_predict(df[["Peso"]])
# print(df)
# data = {
#     "Clienti":["  Anna Rossi","LUCA Bianchi","marTa Verdi  ","Paolo   Neri"],
#     "Email":["anna@gmail.com","luca@","marta@test","paolo@mail.com"],
#     "Telefono":["+39 345 678 9012","345678901","0039-333-222-1111","333 444 555"]
# }
# df = pd.DataFrame(data)
# df["Clienti_Puliti"] = df["Clienti"].str.strip().str.title()
#
# df["Email_Valide"] = df["Email"].str.contains(r"@\w+\.\w+")
# df["Dominio"] = df["Email"].str.extract(r"@(\w+\.\w+)")
#
# df["Telefono_Pulito"] = df["Telefono"].str.replace(r"[^\d]","",regex=True)
#
# print(df["Email_Valide"])
# print(df["Dominio"])
# print(df)
# df = pd.DataFrame({
#     "timestamp":pd.date_range("2025-02-20",periods=6,freq="6h"),
#     "temperatura":[5,6,7,8,6,7]
# })
# df["timestamp"] = pd.to_datetime(df["timestamp"])
# df.set_index("timestamp",inplace=True)
# df_giornaliero = df.resample("D").mean()
# df_giornaliero["giorno_settimana"] = df_giornaliero.index.dayofweek
# df_giornaliero["mese"] = df_giornaliero.index.month
# print(df)
# print(df_giornaliero)
# Esercizio 1
# df = pd.DataFrame({"Nomi":["   Anna verDi", "PAOLO   BiaCHI","martA roSSI   ","luca NERI"]})
# df["Clienti_Puliti"] = df["Nomi"].str.strip().str.title().str.replace(r"  ","",regex=True)
# print(df)

# data = {"Nomi":["Luca","Anna","Paolo","Antonio","Mauro"],
#         "data_nascita":['1995-05-12', '1988-10-30', '2000-03-25', '1992-07-01', '1985-12-15']
#         }
# Esercizio 2
# df = pd.DataFrame(data)
# df["data_nascita"]=pd.to_datetime(df["data_nascita"])
# oggi = pd.Timestamp(date.today())
# df["Eta"] = (oggi - df["data_nascita"]).dt.days // 365
# print(df)

# Esercizio 3

# date_rng = pd.date_range(start="2025-01-01",end="2025-02-28",freq="D")
# df = pd.DataFrame({
#         "Data":date_rng,
#         "Valore":np.random.randint(50,150,size=len(date_rng))
# })
# df.set_index("Data",inplace=True)
# print(df.head())
#
# # media_settimanale = df.resample("W").mean()
# # massimo_mensile = df.resample("ME").max()
# # df["Somma_Cumulativa"] = df["Valore"].cumsum()
# df["avg_7d"] = df["Valore"].rolling(7,min_periods=1).mean()
# df["sum_month"] = df["Valore"].rolling(30).sum()
# print(df)

# print(media_settimanale)
# print(massimo_mensile)
# print(df.head())

# data = {
#     "Cliente": ["anna r.", "LUCA B.", "marta v.", "Paolo n."],
#     "Email": ["anna@mail.com", "lucaa@", "marta@test", "paolo@mail.com"],
#     "Data_ordine": ["2023-01-05", "2023-02-10", "2023-02-20", "2023-03-01"],
#     "Importo": [120.5, 340.0, 215.7, 99.9]
# }
# df = pd.DataFrame(data)
#
# # Pulizia nomi
# df["Cliente"] = df["Cliente"].str.title().str.replace(r"\.", "", regex=True)
#
# # Conversione date e calcolo giorni dall'ordine più recente
# df["Data_ordine"] = pd.to_datetime(df["Data_ordine"])
# df["Giorni_dall_ordine"] = (df["Data_ordine"].max() - df["Data_ordine"]).dt.days
#
# # Validazione email e estrazione dominio
# df["Email_valida"] = df["Email"].str.contains(r"@\w+\.\w+")
# df["Dominio"] = df["Email"].str.extract(r"@(\w+\.\w+)")
#
# print(df.iloc[:,[2,3,4,5,6]])
# Periodo di analisi

# Esercizio
date_rng = pd.date_range(start="2023-09-01", end="2023-12-31", freq="D")

np.random.seed(42)

df = pd.DataFrame({
    "Data": date_rng,
    "Vendite": np.random.randint(80, 200, size=len(date_rng))
})

df = df.set_index("Data")

print(df.head(10))
# Data di inizio promo (evento)
promo_start = pd.Timestamp("2023-10-15")
# promo = (df.index < promo_start) & (df.index >= promo_start + pd.Timedelta(days=27))
prima = (df.index < promo_start) & (df.index >= promo_start - pd.Timedelta(days=28))
dopo = (df.index >= promo_start) & (df.index <= promo_start + pd.Timedelta(days=27))

percentuale = (df[prima].mean() - df[dopo].mean()) / df[prima].mean() * 100
print(percentuale)