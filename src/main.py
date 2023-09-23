from create_filepath import create_filepath
from URLExtractor import URLExtractor
import pandas as pd
from normalizers import CineNormalizer, BibliotecaNormalizer, MuseoNormalizer
from transform import MergeData, CinesData
import settings
import loaders


#CONFIGURACION LOGGING

#DEFINICION DE VARIABLES

urls = {
    "museos": settings.URL_MUSEOS,
    "cines": settings.URL_CINES,
    "bibliotecas": settings.URL_BIBLIOTECAS
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

cines_insights = cine_data.get_insights()


#LOADERS


loaders.MergeDataLoader().load_table(merge_df)
loaders.SizeByCategoryLoader().load_table(count_by_category)
loaders.SizeByProvCatLoader().load_table(count_by_province_category)
loaders.SizeBySourceLoader().load_table(count_by_source)
loaders.CineInsightsLoader().load_table(cines_insights) 