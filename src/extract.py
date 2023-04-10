import os
import requests


def extraer_urls(urls, today, year_month):
    path_museos = extract(today, year_month, urls["museos"], "museos")
    path_bibliotecas = extract(today, year_month, urls["bibliotecas"], "bibliotecas")
    folder = os.path.join("cines", year_month)
    filename = f"cines-{today.strftime('%d-%m-%Y')}.csv"
    path_cines = os.path.join(folder, filename)
    return {"museos": path_museos, "bibliotecas":path_bibliotecas, "cines":path_cines}


def extract(today, year_month, url, name):
        folder = os.path.join(name, year_month)
        os.makedirs(folder, exist_ok=True)
        filename = f"{name}-{today.strftime('%d-%m-%Y')}.csv"
        filepath = os.path.join(folder, filename)
        r = requests.get(url)
        with open(filepath, 'wb') as f:
            f.write(r.content)
        return filepath