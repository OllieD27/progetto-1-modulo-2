import pandas as pd
import numpy as np

# # -------------------------
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
# # 1) CLEAN + FEATURES (SALES)
# # -------------------------
# sales = sales_df.copy()
#
# # Date parsing robusto (formati misti + giorno prima)
# sales["date"] = pd.to_datetime(sales["date"], dayfirst=True, format="mixed", errors="coerce")
#
# # Country standard
# sales["country"] = sales["country"].astype("string").str.strip().str.upper()
#
# # unit_price: gestisce virgole, spazi, None
# # (converte tutto in stringa, replace virgola->punto, poi to_numeric)
# sales["unit_price"] = (
#     sales["unit_price"]
#     .astype("string")
#     .str.strip()
#     .str.replace(",", ".", regex=False)
# )
# sales["unit_price"] = pd.to_numeric(sales["unit_price"], errors="coerce")
#
# # qty: tua regola (no negativi)
# sales["qty"] = sales["qty"].abs()
#
# # imputazione prezzo (come avevi scelto)
# sales["unit_price"] = sales["unit_price"].fillna(sales["unit_price"].median())
#
# # Bucket mensile vendite (datetime al primo giorno del mese)
# sales["month"] = sales["date"].dt.to_period("M").dt.to_timestamp()
#
# # revenue
# sales["revenue"] = sales["qty"] * sales["unit_price"]
#
# # -------------------------
# # 2) SALES_BASE: month-country-product_id
# # -------------------------
# sales_base = (
#     sales.groupby(["month", "country", "product_id"], as_index=False)
#     .agg(
#         total_qty=("qty", "sum"),
#         total_revenue=("revenue", "sum"),
#         n_orders=("order_id", "nunique"),
#     )
# )
#
# # -------------------------
# # 3) SALES_ENRICHED: attach category/brand
# # -------------------------
# sales_enriched = sales_base.merge(products_df, how="left", on="product_id")
# sales_enriched[["category", "brand"]] = sales_enriched[["category", "brand"]].fillna("unknown")
#
# # -------------------------
# # 4) SALES_CAT: month-country-category
# # -------------------------
# sales_cat = (
#     sales_enriched.groupby(["month", "country", "category"], as_index=False)
#     .agg(
#         total_qty=("total_qty", "sum"),
#         total_revenue=("total_revenue", "sum"),
#         n_orders=("n_orders", "sum"),
#     )
# )
#
# # -------------------------
# # 5) RETURNS: build returns_events then returns_cat
# # -------------------------
# returns_ = returns_df.copy()
#
# returns_["return_date"] = pd.to_datetime(returns_["return_date"], errors="coerce")
# returns_["return_month"] = returns_["return_date"].dt.to_period("M").dt.to_timestamp()
#
# # Merge returns -> sales (solo colonne necessarie, così eviti collisioni)
# sales_min = sales[["order_id", "product_id", "country"]].copy()
#
# returns_events = returns_.merge(sales_min, how="inner", on="order_id")
#
# # attacca category
# returns_events = returns_events.merge(products_df[["product_id", "category"]], how="left", on="product_id")
# returns_events["category"] = returns_events["category"].fillna("unknown")
#
# # Aggrega resi a month-country-category (mese del reso)
# returns_cat = (
#     returns_events.groupby(["return_month", "country", "category"], as_index=False)
#     .agg(n_returns=("order_id", "count"))
#     .rename(columns={"return_month": "month"})
# )
#
# # -------------------------
# # 6) CAMPAIGNS: campaigns_mc month-country
# # -------------------------
# campaigns = campaigns_df.copy()
# campaigns["country"] = campaigns["country"].astype("string").str.strip().str.upper()
#
# # month in campaigns: se è "YYYY-MM", questo lo porta al primo giorno del mese
# campaigns["month"] = pd.to_datetime(campaigns["month"], errors="coerce").dt.to_period("M").dt.to_timestamp()
# campaigns["spend"] = pd.to_numeric(campaigns["spend"], errors="coerce")
#
# campaigns_mc = (
#     campaigns.groupby(["month", "country"], as_index=False)
#     .agg(total_spend=("spend", "sum"))
# )
#
# # -------------------------
# # 7) FINAL MERGES
# # -------------------------
# final_report = sales_cat.merge(
#     returns_cat,
#     how="left",
#     on=["month", "country", "category"]
# )
# final_report["n_returns"] = final_report["n_returns"].fillna(0).astype(int)
#
# final_report = final_report.merge(
#     campaigns_mc,
#     how="left",
#     on=["month", "country"]
# )
# final_report["total_spend"] = final_report["total_spend"].fillna(0)
#
# # ROAS (NaN se spend=0)
# final_report["roas"] = np.where(
#     final_report["total_spend"] > 0,
#     final_report["total_revenue"] / final_report["total_spend"],
#     np.nan
# )
#
# final_report = final_report.sort_values(["month", "country", "category"]).reset_index(drop=True)
#
# print(final_report)


# esercizio 3
# df = pd.DataFrame({
#     "Nome":["LUCA","anna  ","  Ruben ","gioRgio","Tony","Elena"],
#     "Email":["luca@mail","anna@gmail.com","RUben@","tony@gmail.com","elena@test.com","test@test"],
#     "Data_iscrizione":["2025-01-05","2025/01/05","05-01-2025","2025-01-12","2025-02-02","2025-02-15"],
#     "Eta":[23,"34","34",23,33,25],
#     "Stipendio":[1500,2000,None,1740,1699,2100],
#     "Citta":["Roma","Milano","Napoli",None,"Firenze","Spezia"],
#     "Prodotto":["P1","P3","P2","P4","P5","P6"],
#     "Categoria":["Cat1","Cat2","Cat3","Cat2","Cat1","Cat4"],
#     "Vendite":[150,70,700,200,200,360],
#     "Giorni_attivi":[10,4,None,5,6,20]
# })
#
# df_pulito = df.copy()
#
# # Pulizia stringhe e dati
# df_pulito["Nome"] = df_pulito["Nome"].map(lambda x:x.strip().title() if pd.notnull(x) else x)
# df_pulito["Eta"] = pd.to_numeric(df_pulito["Eta"],downcast="integer")
#
# df_pulito["Email_valide"] = df_pulito["Email"].str.contains(r"@\w+\.\w+")
# df_pulito["Dominio"] = df_pulito["Email"].str.extract(r"@(\w+\.\w+)")
#
# df_pulito["Data_iscrizione"] = pd.to_datetime(df_pulito["Data_iscrizione"],dayfirst=True,format="mixed")
# oggi = pd.Timestamp.today()
# df_pulito["Giorni_dalla_iscrizione"] = (oggi - df_pulito["Data_iscrizione"]).dt.days
# print(df_pulito["Giorni_dalla_iscrizione"])
# df_pulito.set_index("Data_iscrizione",inplace=True)
#
# # Gestione None e Outlier
# df_pulito["Stipendio"] = df_pulito["Stipendio"].fillna(df_pulito["Stipendio"].median())
# df_pulito["Giorni_attivi"] = df_pulito["Giorni_attivi"].fillna(df_pulito["Giorni_attivi"].median())
# df_pulito["Citta"] = df_pulito["Citta"].where(pd.notnull(df_pulito["Citta"]),"Unknown")
#
# # Gestione Outlier con IQR
# Q1 = df_pulito["Vendite"].quantile(0.25)
# Q3 = df_pulito["Vendite"].quantile(0.75)
# IQR = Q3 - Q1
# lower_value = Q1 - 1.5 * IQR
# upper_value = Q3 + 1.5 * IQR
# df_pulito["Outlier_vendite"] = (df_pulito["Vendite"] < lower_value) | (df_pulito["Vendite"] > upper_value)
#
#
# # Gestione Outlier con condizione, supponiamo che i giorni attivi siano massimo 10
# df_pulito["Outlier_giorni_attivi"] = np.where(df_pulito["Giorni_attivi"] > 10,True,False)
#
# media_sett = df_pulito.groupby(["Categoria","Prodotto"]).resample("W")["Vendite"].count()
# massimo_mensile = df_pulito.groupby(["Categoria","Prodotto"]).resample("ME")["Vendite"].count()
# print(media_sett)
# print(massimo_mensile)
# df_pulito['Log_Stipendio'] = np.log1p(df_pulito['Stipendio'])
# print(df_pulito["Log_Stipendio"])