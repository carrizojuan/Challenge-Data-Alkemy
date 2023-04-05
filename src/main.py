from datetime import datetime
import os
from extract import extraer_urls
from transform import merge_dfs, getCineInsights
from loaders import MergeDataLoader, SizeByCategoryLoader, SizeByProvCatLoader, SizeBySourceLoader, CineInsightsLoader
import logging
import logging.handlers

logger = logging.getLogger()
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Configuramos el logger root para escribir los mensajes a un archivo
#logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Creamos un handler RotatingFileHandler para permitir la rotación de archivos
file_handler = logging.handlers.RotatingFileHandler(filename='logs.log', maxBytes=1024)
file_handler.setFormatter(formatter)

# Agregamos el handler al logger root
logger.addHandler(file_handler)




urls = {
    "museos": "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv",
    "cines": "https://datos.cultura.gob.ar/dataset/0560ef96-55ca-4026-b70a-d638e1541c05/resource/b8bf0459-16a5-430b-b8e1-4fb786572469/download/salas_cine.csv",
    "bibliotecas": "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv"
}

#Obtencion fecha actual

today = datetime.now()
year_month = today.strftime('%Y-%B')

logger.info("Extrayendo urls...")
try:
    paths = extraer_urls(urls, today, year_month)
    logger.info("Urls extraidas con éxito")
except:
    logger.error("No se pudo extraer las urls")


filename = f"merge-{today.strftime('%d-%m-%Y')}.csv"
folder_merge = os.path.join("merges", year_month)
merge_path = os.path.join(folder_merge, filename)
os.makedirs(folder_merge, exist_ok=True) 

logger.info("Mergeando datasets")

try:
    merge_data = merge_dfs(paths, merge_path)
    logger.info("Datasets mergeados con éxito")
except ValueError:
    logger.error("No se pudo mergear los datasets", ValueError)

size_by_category = merge_data.getSizeByCategory()
size_by_prov_cat = merge_data.getSizeByProvinceCategory()
size_by_source = merge_data.getSizeBySource()

cines_insights = getCineInsights(paths["cines"])


MergeDataLoader().load_table(merge_data.getDF())
SizeByCategoryLoader().load_table(size_by_category)
SizeByProvCatLoader().load_table(size_by_prov_cat)
SizeBySourceLoader().load_table(size_by_source)
CineInsightsLoader().load_table(cines_insights)