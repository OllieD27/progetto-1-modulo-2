import pandas as pd
import numpy as np

data = {
    "Data": [
        "2023-10-01", "2023-10-01","2023-10-02","2023-10-03","2023-10-05","2023-10-06","2023-10-07",
        "2023-10-07","2023-10-08",None],
    "Prodotto": [
        "A101","A101","A101","B205","B205","B205","A101","A101",None,"C333"],
    "Vendite": [10,10,12,5,None,7,20,20,-3,8],
    "Prezzo": [9.99,9.99,9.99,15.50,15.50,None,9.99,9.99,9.99,0]
}

df = pd.DataFrame(data)

########################### Parte 1 ###########################
                                                              #
print("Le prime 5 righe del DF\n")                            #
print(df.head(5))                                             #
print("La struttura del DF\n")                                #
print(df.info())                                              #
print("Le Statistiche descrittive del DF\n")                  #
print(df.describe())                                          #
                                                              #
########################### Parte 2 ###########################
# Pulizia DF                                                  #
df["Data"] = pd.to_datetime(df["Data"])                       #   #Conversione del Data in datetime
df.set_index(df["Data"])                                      #   #Impostare Data come indice del DF
df["Prodotto"] = df["Prodotto"].fillna("Unknown")             #   #Impostare il valore None del Prodotto con Unknown
df["Vendite"] = df["Vendite"].fillna(0)                       #   #Impostare il valore None delle Vendite con 0
df["Vendite"] = df["Vendite"].where(df["Vendite"] > 0,0)      #   #Sostituzione con 0 ogni valore negativo trattandosi di un errore
df["Prezzo"] = df["Prezzo"].fillna(df["Prezzo"].median())     #   #Impostare il valore None del Prezzo con la mediana
df["Prezzo"] = df["Prezzo"].where(df["Prezzo"] > 0,0)         #   #Sostituzione con 0 ogni valore negativo trattandosi di un errore

# Per analisi del DF i duplicati non vanno eliminati per non perdere informazione.

########################### Parte 3 ###########################
# Analisi esplorativa del DF
vendite_tot_prodotto = df.groupby("Prodotto")["Vendite"].sum()
# Vendite Totali per ogni prodotto
print(vendite_tot_prodotto)
# Prodotto piu venduto
prodotto_piu_venduto = df.groupby("Prodotto")["Vendite"].sum().idxmax()
print(f"Il prodotto piu venduto e stato: {prodotto_piu_venduto}")
# Prodotto meno venduto
prodotto_meno_venduto = df.groupby("Prodotto")["Vendite"].sum().idxmin()
print(f"Il prodotto meno venduto e stato: {prodotto_meno_venduto}")
# La media giornaliera di vendite
media_giorno = df.groupby("Vendite")["Prezzo"].mean()
print(media_giorno)