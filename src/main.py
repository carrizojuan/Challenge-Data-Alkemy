from create_filepath import create_filepath
import os
from URLExtractor import URLExtractor
import pandas as pd
from normalizers import CineNormalizer, BibliotecaNormalizer, MuseoNormalizer
from transform import MergeData, CinesData
#from loaders import MergeDataLoader, SizeByCategoryLoader, SizeByProvCatLoader, SizeBySourceLoader, CineInsightsLoader


#CONFIGURACION LOGGING

""" logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# Creamos un handler RotatingFileHandler para permitir la rotación de archivos
file_handler = logging.handlers.RotatingFileHandler(filename='logs.log', maxBytes=1024)
file_handler.setFormatter(formatter)
# Agregamos el handler al logger root
logger.addHandler(file_handler) """


#DEFINICION DE VARIABLES

urls = {
    "museos": "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv",
    "cines": "https://datos.cultura.gob.ar/dataset/0560ef96-55ca-4026-b70a-d638e1541c05/resource/b8bf0459-16a5-430b-b8e1-4fb786572469/download/salas_cine.csv",
    "bibliotecas": "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv"
}


#EXTRACT PROCES

filepaths = {}

#logger.info("Extrayendo...")
try:
    extractor = URLExtractor()
    for name, url in urls.items():
        filepaths[name] = extractor.extract(url, name)    
    #logger.info("Urls extraidas con éxito")
except:
    #logger.error("No se pudo extraer las urls")
    print("error")


#TRANSFORM

#creating dataframes to normalize
dfs = {}
for name, filepath in filepaths.items():
    dfs[name] = pd.read_csv(filepath)

#defining normalizers for every dataframe
normalizers = {}
normalizers["museos"] = MuseoNormalizer(dfs["museos"])
normalizers["bibliotecas"] = BibliotecaNormalizer(dfs["bibliotecas"])
normalizers["cines"] = CineNormalizer(dfs["cines"])

#normalizing dataframes
norm_dfs = []
for name, normalizer in normalizers.items():
    norm_dfs.append(normalizer.normalize())



#merging data
merge_path = create_filepath("merges")
merge_df = pd.concat(norm_dfs, axis=0, ignore_index=True)
merge_df.to_csv(merge_path)

#Analytics from merging data
merge_data = MergeData(merge_df, dfs)


#ANALISIS DE MERGE DATA

#Count by category

count_by_category = merge_data.get_count_by_category()

#COUNT BY SOURCE

count_by_source = merge_data.get_count_by_source()

#COUNT BY PROVINCE AND CATEGORY

count_by_province_category = merge_data.get_count_by_province_category()


#CINES ANALISIS

cine_data = CinesData(dfs["cines"])

cines_insights = cine_data.get_insights_table()

print(cines_insights)


""" MergeDataLoader().load_table(merge_data.getDF())
SizeByCategoryLoader().load_table(size_by_category)
SizeByProvCatLoader().load_table(size_by_prov_cat)
SizeBySourceLoader().load_table(size_by_source)
CineInsightsLoader().load_table(cines_insights)  """