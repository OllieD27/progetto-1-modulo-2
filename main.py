import pandas as pd
import numpy as np
import hashlib
import matplotlib.pyplot as plt
import time
from pandas.core.interchange.dataframe_protocol import DataFrame
# from sklearn.impute import KNNImputer
# from sklearn.impute import IterativeImputer
# from sklearn.experimental import enable_iterative_imputer
from sklearn.ensemble import IsolationForest
from datetime import date,datetime

# Esercizio 1
# data = {
#     "Nome":["anna","LUCA",None,"Paolo","Marta"],
#     "Email":[" anna@mail.com ","LUCA@",None,"paolo@mail.com","marta@test"],
#     "Eta":[25,None,30,28,None],
#     "Paese":["IT","IT","FR","IT","ES"]
# }
#
# df = pd.DataFrame(data)
# df["Nome"] = df["Nome"].map(lambda x:x.strip().capitalize() if pd.notnull(x) else x)
# df["Email"] = df["Email"].map(lambda x:x.strip().lower() if pd.notnull(x) else x)
# df["Email_valida"] = df["Email"].str.contains(r"^\w+[\.-]?\w+@\w+\.\w+$",na=False)
# df["Eta"] = df["Eta"].fillna(df["Eta"].median())
# df["Paese"] = df["Paese"].astype("category")
# summary = df.isna().sum().to_dict()
# print(df)
# print(summary)

# Esercizio 2
# data = {
#     "Store":["S1","S2","S1","S3","S2"],
#     "Prodotto":["P1","P2","P1","P3","P2"],
#     "Data":["2023-01-01","2023-01-02","2023-01-08","2023-02-01","2023-02-10"],
#     "Vendite":[100,200,150,300,250]
# }
# df = pd.DataFrame(data)
# df["Store"].astype("category")
# df["Prodotto"].astype("category")
# df["Data"] = pd.to_datetime(df["Data"])
# df = df.set_index("Data")
#
# settimanale = df.groupby(["Store","Prodotto"]).resample("W")["Vendite"].sum()
# mensile = df.groupby(["Store","Prodotto"]).resample("ME")["Vendite"].mean()
# print(settimanale)
# print(mensile)

# Q1 = mensile.quantile(0.25)
# Q3 = mensile.quantile(0.75)
# IQR = Q3 - Q1
# outliers = mensile[(mensile < Q1 - 1.5 * IQR) | (mensile > Q3 + 1.5 * IQR)]
# df["Vendite"] = pd.to_numeric(df["Vendite"],downcast="integer")
#
# print(df)
# Esercizio 3
# data = {
#     "timestamp":["2023-03-01T12:00:00Z","2023-03-01T12:01:30Z","2023-03-01T13:05:00Z"],
#     "user_id":[1,2,1],
#     "amount":[10.0,5.0,7.5]
# }
# df = pd.DataFrame(data)
# df["timestamp"]= pd.to_datetime(df["timestamp"],utc=True)
# df["timestamp_local"] = df["timestamp"].dt.tz_convert("Europe/Rome").dt.round("min")
# df = df.set_index(df["timestamp_local"].sort_index())
# series = df.resample("min").agg({"amount":"sum","user_id":"count"}).fillna(0)
# series["sum_24h"] = series["amount"].rolling(24*60,min_periods=1).sum()
# series["avg_7d"] = series["amount"].rolling(7*24*60,min_periods=1).mean()
# print(series)
#
# # #

# Esercizio 1 - Dataset clienti
# data = {
#     "Nome":["anna ","LAURA","luCa  ","Fabio",None,],
#     "Email":["anna@gmail.com","LAURA@ ","luca@gmail.com",None,"test@test"],
#     "Data_nascita":["1992-01-02","1994-02-23","2005-02-02","2002-06-04","2000-04-04"],
#     "Eta":[30,20,None,23,32],
#     "Stipendio":np.random.uniform(1000,5000,size=5),
#     "Citta":["Roma","Milano","Torino","Milano","Firenze"]
# }
# df = pd.DataFrame(data)
# df["Nome"] = df["Nome"].map(lambda x:x.strip().title() if pd.notnull(x) else x)
# df["Email"] = df["Email"].map(lambda x: x.strip().lower() if pd.notnull(x) else x)
# df["Email_validate"] = df["Email"].str.contains(r"^\w+[\.-]?\w+@\w+\.\w+$",na=False)
# df["Data_nascita"] = pd.to_datetime(df["Data_nascita"])
# df["Eta"] = df["Eta"].fillna(df["Eta"].median())
# df["Stipendio"] = df["Stipendio"].astype(dtype=np.int32)
# df["Citta"] = df["Citta"].astype("category")
#
# df["Eta_reale"] =  date.today().year - df["Data_nascita"].dt.year
# print(df[["Eta","Eta_reale"]])
# Q1 = df["Eta_reale"].quantile(0.25)
# Q3 = df["Eta_reale"].quantile(0.75)
# IQR = Q3 - Q1
# lower = Q1 - 1.5 * IQR
# upper = Q3 + 1.5 * IQR
# df["Outlier"] = ((df["Eta_reale"] < lower) | (df["Eta_reale"] > upper))
# print(df)

# Esercizio 2 - Dataset Vendite
# data = {
#     "Prodotto":["P1","P2","P3","P4","P2","P1","P3"],
#     "Categoria":["Elettronica","Casa","Abbigliamento","Giardino","Cucina","DYI","Auto"],
#     "Prezzo":[400,140,200,50,170,100,430],
#     "Quantita":[3,2,5,1,7,4,20],
#     "Data_vendita": pd.date_range("2025-01-01","2025-01-6",periods=7)
# }
# df = pd.DataFrame(data)
# date_rng = pd.date_range(start="2023-01-01", end="2023-03-31", freq="D")
# df = pd.DataFrame({
#     "Data": date_rng,
#     "Vendite": np.random.randint(50, 500, size=len(date_rng))
# })
#
# # Conversione e calcoli temporali
# df["Data"] = pd.to_datetime(df["Data"])
# df["Settimana"] = df["Data"].dt.isocalendar().week
# df["Giorno_settimana"] = df["Data"].dt.day_name()
# df["Vendite_cumulative"] = df["Vendite"].cumsum()
# df["Delta_gg"] = (df["Data"] - df["Data"].min()).dt.days
#
# # Resampling settimanale e mensile
# df.set_index("Data", inplace=True)
# settimanale = df["Vendite"].resample("W").mean()
# mensile = df["Vendite"].resample("ME").sum()
# print(settimanale.head())
# print(mensile.head())
# print(mensile)

# data = {"customer_id":np.arange(1,6),
#         "age":[25,None,120,30,28],
#         "income":[30_000,45_000,1_000_000,None,32_000],
#         "country":["IT","FR","IT","DE","XX"]
#         }
# df = pd.DataFrame(data)
#
# df["age"] = df["age"].fillna(df["age"].median())
# max_age = df["age"].max()
# df["age"] = df["age"].where(df["age"] < max_age).fillna(df["age"].median())
#
# Q1 = df["income"].quantile(0.25)
# Q3 = df["income"].quantile(0.75)
# IQR = Q3 - Q1
#
# lower = Q1 - 1.5 * IQR
# upper = Q3 + 1.5 * IQR
# mask = (df["income"] < lower) | (df["income"] > upper)
# df["income"] = df["income"].fillna(df["income"].median())
# df["outlier"] = mask
# df["premium"] = np.where(df["income"] > 100_000,"Premium","Not Premium")
#
# mask_2 = df["country"].str.contains(r"^\b[X-x]",na=False)
# df["country"] = df["country"].mask(mask_2).fillna("Not Valid")
#
# df["country"] = df["country"].astype("category")
# df["age"] = df["age"].astype(dtype=np.int8)
# print(df)


# data = {
#         "order_id":np.arange(1,8),
#         "user_id":[10,11,10,12,13,11,14],
#         "amount":[25,30,500,28,None,27,26],
#         "days_since_signup":[5,2,5,3000,10,2,None],
#         "channel":["web","app","web","web","store","app","unknown"]
# }
# df = pd.DataFrame(data)
# # Imputazione NaN
# df["amount"] = df["amount"].fillna(df["amount"].median())
# df["days_since_signup"] = df["days_since_signup"].fillna(df["days_since_signup"].median())
# # Rilevazione outlier Amount
# Q1 = df["amount"].quantile(0.25)
# Q3 = df["amount"].quantile(0.75)
# IQR = Q3 - Q1
# lower = Q1 - 1.5 * IQR
# upper = Q3 + 1.5 * IQR
# mask = (df["amount"] < lower) | (df["amount"] > upper)
# df["amount_outlier"] = mask
# df["premium"] = np.where(mask,"Premium","Not Premium")
# # Rilevazione Outlier con condizione di days_since_signup
# # Supponiamo che abbiamo cominciato con le registrazioni da 10 giorni
# df["days_since_signup"] = df["days_since_signup"].where(df["days_since_signup"] <= 10,df["days_since_signup"].median())
# # Cambio di categoria delle channel da unknown a other
# df["channel_grouped"] = df["channel"].where(df["channel"] != "unknown","other")
# # Ottimizzazione df
# df["order_id"] = df["order_id"].astype(dtype=np.int8)
# df["user_id"] = df["user_id"].astype(dtype=np.int16)
# df["amount"] = df["amount"].astype(dtype=np.float32)
# df["days_since_signup"] = df["days_since_signup"].astype(dtype=np.float32)
# df["channel"] = df["channel"].astype("category")
# df["channel_grouped"] = df["channel_grouped"].astype("category")
# print(df)

# Esempio Data set con dati mescolati e separazione value e eventi
# data = {
#     "event_id":np.arange(1,8),
#     "user_id":[100,100,101,102,103,100,104],
#     "event_type":["click","purchase","purchase","click","purchase","purchase","click"],
#     "value":[1,20,2000,1,None,25,1],
#     "days_from_start":[1,1,2,400,3,1,None]
# }
# df = pd.DataFrame(data)
#
# # Imputazione NaN
# df["days_from_start"] = df["days_from_start"].fillna(df["days_from_start"].median())
# df["value"] = df["value"].fillna(df["value"].median())
#
# # Separazione Eventi e value
# df["click_event"] = np.where(df["event_type"] == "click", df["value"],np.nan)
# df["purchase_value"] = np.where(df["event_type"] == "purchase",df["value"],np.nan)
#
# # Flag eventi click e purchase
# df["is_click"] = np.where(df["click_event"] == 1,True,False)
# df["is_premium_client"] = np.where(df["purchase_value"] > 1000,True,False)
#
# # Rilevazione di flag di days from start
# df["invalid_day_flag"] = df["days_from_start"] > 10
#
# # Correzione Day From Start con la mediana
# df["days_from_start_clean"] = df["days_from_start"].where(df["days_from_start"] <= 10,df["days_from_start"].median())
#
# # Ottimizzazione e Downcasting del DF
# # print("Info del DF prima del downcasting: \n")
# # print(df.info(memory_usage="deep"))
# # initial_memory = df.memory_usage(deep=True).sum() // 1024 ** 2
# # print(f"Memoria iniziale prima del downcasting: {initial_memory:.2f} Mb")
# #
# # df["event_id"] = df["event_id"].astype(dtype=np.int16)
# # df["user_id"] = df["user_id"].astype(dtype=np.int32)
# # df["event_type"] = df["event_type"].astype("category")
# # df["value"] = df["value"].astype(dtype=np.float32)
# # df["days_from_start"] = df["days_from_start"].astype(dtype=np.int16)
# # df["days_from_start_clean"] = df["days_from_start_clean"].astype(dtype=np.int16)
# #
# # final_memory = df.memory_usage(deep=True).sum() // 1024 ** 2
# # print(f"Memoria finale dopo il downcasting: {final_memory:.2f} MB")
# # print(f"Ottimizzazione della memoria: {(initial_memory - final_memory):.2f} MB")
# # print(df.info(memory_usage="deep"))
# print(df)

# Esercizio con aggregazioni e DF pulito
# df = pd.DataFrame({
#     "user_id": [1, 1, 1, 2, 2, 3, 3, 3, 3],
#     "event_type": ["click", "purchase", "purchase",
#                    "click", "purchase",
#                    "click", "click", "purchase", "purchase"],
#     "amount": [np.nan, 20, 30,
#                np.nan, 15,
#                np.nan, np.nan, 40, 1000],
#     "event_date": pd.to_datetime([
#         "2023-01-01",
#         "2023-01-05",
#         "2023-02-01",
#         "2023-01-10",
#         "2023-02-20",
#         "2023-01-03",
#         "2023-01-04",
#         "2023-03-01",
#         "2023-03-10"
#     ])
# })
# # Separazione Eventi in due Series diverse
# df["purchase_event"] = np.where(df["event_type"] == "purchase",df["event_type"],None)
# df["click_event"] = np.where(df["event_type"] == "click",df["event_type"],None)
# # Feature di maschera booleana per eventi purchase
# df["is_purchase"] = df["event_type"] == "purchase"
#
# # Flag High Spender
# df["high_value_purchase"] = df["amount"] > 500
# mask = df["amount"] > 500
#
# # Df User pulito con le aggregazioni
# df_user = (df.groupby("user_id").agg(
#     purchase_count=("amount","count"),
#     total_spend=("amount","sum"),
#     last_event_date=("event_date","max"),
#     high_value_flag=("high_value_purchase","any")
# ))
# df_user["avg_ticket"] = df_user["total_spend"] / df_user["purchase_count"]
# print(df)
# print(df_user)

# sales_df = pd.DataFrame({
#     "order_id":np.arange(1001,1009),
#     "date":["2025-01-05","2025/01/05","05-01-2025","2025-01-12","2025-02-02","2025-02-15","2025-02-28","2025-03-01"],
#     "product_id":["P01","P02","P03","P02","P04","P03","P99","P01"],
#     "qty":[2,1,3,-1,2,1,1,1],
#     "unit_price":["9.99","19.90","5.5"," 19,90 ",None,"5.5","12.00","9.99"],
#     "country":["IT","it","FR","IT","DE","FR","IT","IT"],
# })
#
# products_df = pd.DataFrame({
#     "product_id":["P01","P02","P03","P04","P05"],
#     "category":["accessories","electronics","accessories","home","electronics"],
#     "brand":["Acme","Acme","Bee","Bee","Delta"]
# })
#
# returns_df = pd.DataFrame({
#     "order_id":[1002,1004,9999],
#     "return_date":["2025-01-20","2025-01-15","2025-02-10"],
#     "reason":["damaged","wrong_item","unknown"]
# })
#
# campaigns_df = pd.DataFrame({
#     "month":["2025-01","2025-01","2025-02","2025-02","2025-02","2025-03"],
#     "country":["IT","FR","IT","FR","DE","IT"],
#     "spend":["1000","700","1200","650","300","400"]
# })
#
# # Pulizia Sales DF
# # Conversione a datetime della Series date con una funzione lambda che converte in strftime ogni oggetto x datetime e lo riformatta.
# sales_df["date"] = pd.to_datetime(sales_df["date"],dayfirst=True,format="mixed")
# sales_df["country"] = sales_df["country"].map(lambda x:x.strip().upper() if pd.notnull(x) else x)
#
# # Conversione del tipo da str obj a np.float32
# sales_df["unit_price"] = sales_df["unit_price"].str.replace(",",".")
# sales_df["unit_price"] = sales_df["unit_price"].astype(dtype=np.float32)
#
#
# # Regola per quantity ogni valore deve essere positivo, non puo esistere una quantita negativa.
# sales_df["qty"] = sales_df["qty"].where(sales_df["qty"] > 0,0)
# # Feature eng
# sales_df["sales_month"] = pd.to_datetime(sales_df["date"])
# sales_df["revenue"] = sales_df["qty"] * sales_df["unit_price"]
#
# # Pulizia Returns DF
# returns_df["return_date"] = pd.to_datetime(returns_df["return_date"])
# returns_df["return_month"] = pd.to_datetime(returns_df["return_date"])
# # Pulizia Campaigns DF
# campaigns_df["month"] = pd.to_datetime(campaigns_df["month"])
# campaigns_df["country"] = campaigns_df["country"].map(lambda x:x.strip().upper() if pd.notnull(x) else x)
# campaigns_df["spend"] = campaigns_df["spend"].astype(dtype=np.float32)
#
# products_df["product_id"] = products_df["product_id"].drop_duplicates()
#
#
# sales_base = (sales_df.groupby(["sales_month","country","product_id"],as_index=False).agg(
#     total_qty=("qty","sum"),
#     total_revenue=("revenue","sum"),
# ))
#
# sales_enriched = sales_base.merge(products_df,how="left",on="product_id")
# sales_enriched[["category","brand"]] = sales_enriched[["category","brand"]].fillna("unknown")
#
# sales_cat = sales_enriched.groupby(["sales_month","country","category"],as_index=False).agg(
#     total_qty=("total_qty","sum"),
#     total_revenue=("total_revenue","sum")
# )
#
#
# returns_base =  returns_df.merge(sales_df,how="inner",on="order_id")
# return_enriched = returns_base.merge(products_df,how="left",on="product_id")
# return_enriched["return_month"] = return_enriched["return_date"].dt.to_period("M").dt.to_timestamp()
#
# return_cat = return_enriched.groupby(["return_month","country","category"],as_index=False).agg(
#     n_returns=("order_id","count")
# )
#
# campaigns_mc = campaigns_df.groupby(["month","country"] , as_index=False).agg(
#     total_spend=("spend","sum")
# )
# # print(campaigns_mc)
# final_report = sales_cat.merge(return_cat,how="left",on=["country","category"])
# # final_report = final_report.merge(campaigns_mc,how="inner",on="country")
# print(final_report.shape)