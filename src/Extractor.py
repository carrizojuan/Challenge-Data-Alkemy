import requests
import os


class Extractor:
    
    def extract(self, today, year_month, url, name):
        folder = os.path.join(name, year_month)
        os.makedirs(folder, exist_ok=True)
        filename = f"{name}-{today.strftime('%d-%m-%Y')}.csv"
        filepath = os.path.join(folder, filename)
        r = requests.get(url)
        with open(filepath, 'wb') as f:
            f.write(r.content)
        return filepath
