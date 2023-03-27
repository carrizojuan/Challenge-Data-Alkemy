import requests
import pandas as pd
import io
from datetime import datetime
import os

url_museos = "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv"
url_cines = "https://datos.cultura.gob.ar/dataset/0560ef96-55ca-4026-b70a-d638e1541c05/resource/b8bf0459-16a5-430b-b8e1-4fb786572469/download/salas_cine.csv"
url_bibliotecas = "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv"

today = datetime.now()
year_month = today.strftime('%Y-%B')

def extract(url, tipo):
    folder = os.path.join(tipo, year_month)
    os.makedirs(folder, exist_ok=True)
    filename = f"{tipo}-{today.strftime('%d-%m-%Y')}.csv"
    filepath = os.path.join(folder, filename)
    r = requests.get(url)
    with open(filepath, 'wb') as f:
        f.write(r.content)

""" def extract(path):
    data = pd.read_csv(path, delimiter=",")
    return data """

""" def exportar_data(data):
    to_path = os.path.join(os.path.dirname(__file__), data['nombre'], "2022-septiembre", data['nombre']+"csv")
    data.to_csv(to_path) """

extract(url_museos, "museos")

#data_museos = extract("museos.csv")


#print(data_museos.iloc[0,0])
#año_mes = "2022-septiembre"
#dia_mes_año = "23/09/2022"

#print(data_museos)
#print(data_museos[data_museos['Cod_Loc'] == 6588100])

#data_museos.to_csv("museos/2021-noviembre/museos-03-11-2021.csv")
#exportar_data(data_museos)

""" 
to_path = os.path.join(os.path.dirname(__file__), "museos", "2022-septiembre")
print(to_path)
os.makedirs(to_path, exist_ok=True)

data_museos.to_csv(f"{to_path}/museos-23-09-2022.csv", encoding="utf-8") """