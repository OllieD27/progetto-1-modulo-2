# df = pd.DataFrame({
#     "id":np.arange(1,1_000_001,dtype=np.int64),
#     "nome":np.random.choice(["Alice","Bob","Carla","David"],size=1_000_000),
#     "salary":np.random.uniform(1000,5000,size=1_000_000)
# })
#
# df.to_csv("data.csv",index=False)
#
# df = pd.read_csv("data.csv",usecols=["id","salary","nome"])
# df = df.drop_duplicates().dropna(subset=["salary"])
# df["id"] = df["id"].astype(np.int32)
# df["salary"] = df["salary"].astype(np.float32)
#
# print(df.info(memory_usage="deep"))
#
# salt = "my_salt123"
# df["nome_hmac"] = df["nome"].map(
#     lambda x:hashlib.sha256((salt + x).encode()).hexdigest()
# )
#
# print(df.head())
# df = df.set_index("id")
# print(df.loc[5000])
#
# mean_salary = df.groupby("nome_hmac")["salary"].mean()
# print(mean_salary.head())
# Esercizio 1
# df = pd.DataFrame({
#     "id":np.arange(1,500_001,dtype=np.int64),
#     "nome":np.random.choice(["Luca","Antonio","Mauro","Sara","Angela"],size=500_000),
#     "salary":np.random.uniform(1000,5000,size=500_000)
# })
# df.to_csv("data_1",index=False)
# Lettura del csv e caricamento delle colonne necessarie
# df = pd.read_csv("data_1", usecols=["id", "nome", "salary"])
# df.drop_duplicates().dropna(subset="salary")
#
# salt = "mysalt123"
# df["nome_hmac"] = df["nome"].map(
#     lambda x: hashlib.sha256((salt + x).encode()).hexdigest()
# )
# df.set_index("id")
# print(df.info(memory_usage="deep"))
# memoria_iniziale = df.memory_usage(deep=True).sum() // 1024 ** 2
# print(f"Memoria iniziale prima del downcasting: {memoria_iniziale:.2f} MB")
# df["id"] = pd.to_numeric(df["id"],downcast="integer")
# df["nome"] = df["nome"].astype("category")
# df["salary"] = pd.to_numeric(df["salary"],downcast="float")
#
# memoria_finale = df.memory_usage(deep=True).sum() // 1024 ** 2
#
# print(df.info(memory_usage="deep"))
# print(f"Memoria finale dopo il downcasting: {memoria_finale:.2f} MB")
# print(f"Ottimizzazione della mememoria: {(memoria_iniziale - memoria_finale):.2f}")

# Esercizio 2
# df = pd.DataFrame({
#     "Interi": np.random.randint(10,10_000,size=1_000_000,dtype="int64"),
#     "Decimali":np.random.rand(1_000_000) * 1000
# })
# # Calcolo prima del downcasting
# print("Info del DF prima del downcasting:\n")
# print(df.info(memory_usage="deep"))
# memoria_iniziale = df.memory_usage(deep=True).sum() // 1024 ** 2
# print(f"Memoria Iniziale prima del downcasting: {memoria_iniziale:.2f} MB")
# start_time = time.time()
# print(df.groupby("Interi")["Decimali"].sum())
# tempo_di_calcolo = time.time() - start_time
# print(f"Tempo di calcolo {tempo_di_calcolo:.5f} Secondi")
#
# # Downcasting del DF
# df["Interi"] = df["Interi"].astype(np.int32)
# df["Decimali"] = df["Decimali"].astype(np.float32)
# print("Info del DF dopo il downcasting:\n")
#
# start_time = time.time()
# print(df.groupby("Interi")["Decimali"].sum())
# tempo_di_calcolo = time.time() - start_time
# print(f"Tempo di calcolo dopo il downcasting:{tempo_di_calcolo:.5f} Secondi")
# print(df.info(memory_usage="deep"))
# memoria_finale = df.memory_usage(deep=True).sum() // 1024 ** 2
# print(f"Memoria finale dopo il downcasting: {memoria_finale:.2f} MB")
# print(f"Ottimizzazione della memoria: {(memoria_iniziale - memoria_finale):.2f} MB")

# n = 1_000_000
# salt = "my_salt_123"
# df = pd.DataFrame({
#     "id":np.arange(1,n + 1,dtype=np.int64),
#     "name":np.random.choice(["Luca","Mauro","Angelo","Fabio"],size=n),
#     "salary":np.random.uniform(1000,5000,size=n),
#     "city":np.random.choice(["Roma","Milano","Torino","Firenze"],size=n),
#     "department":np.random.choice(["HR","Marketing","Amministrazione","Tech"])
# })
#
# # Pulizia valori ripetuti e mancanti
# df.drop_duplicates()
# df.dropna(subset="salary")
# # Impostazione del indice con i valori del ID
# df.set_index("id")
#
# df["name_hmac"] = df["name"].map(
#     lambda x: hashlib.sha256((salt + x).encode()).hexdigest()
# )
# # Info del DF e del uso di memoria
# print(df.info(memory_usage="deep"))
# memoria_iniziale = df.memory_usage(deep=True).sum() // 1024 ** 2
# print(f"Memoria inziale del df {memoria_iniziale:.2f} MB")
# time_pre = time.time()
# media_stipendio = df.groupby("name")["salary"].mean()
# end_time = time.time() - time_pre
# print(f"Tempo di operazione pre ottimizzazione: {end_time:.5f} Secondi")
#
#
# # Conversione delle colonne in categorie
# df["id"] = pd.to_numeric(df["id"],downcast="integer")
# df["name"] = df["name"].astype("category")
# df["salary"] = pd.to_numeric(df["salary"],downcast="float")
# df["city"] = df["city"].astype("category")
# df["department"] = df["department"].astype("category")
#
# # Info del DF dopo l'ottimizzazione
# print(df.info(memory_usage="deep"))
# memoria_finale = df.memory_usage(deep=True).sum() // 1024 **2
# print(f"Memoria finale dopo l'ottimizzazione: {memoria_finale:.2f}MB")
# print(f"Memoria ottimizzata dopo la conversione: {(memoria_iniziale - memoria_finale):.2f} MB")
#
# time_post = time.time()
# media_stipendio_post = df.groupby("name")["salary"].mean()
# end_time_post = time.time() - time_post
# print(f"Tempo di operazione dopo l'ottimizzazione: {end_time_post:.5f} Secondi")