from Extractor import Extractor
import os


def extraer_urls(urls, today, year_month):
    extractor = Extractor() 
    path_museos = extractor.extract(today, year_month, urls["museos"], "museos")
    path_bibliotecas = extractor.extract(today, year_month, urls["bibliotecas"], "bibliotecas")
    folder = os.path.join("cines", year_month)
    filename = f"cines-{today.strftime('%d-%m-%Y')}.csv"
    path_cines = os.path.join(folder, filename)
    return {"museos": path_museos, "bibliotecas":path_bibliotecas, "cines":path_cines}