import requests
from create_filepath import create_filepath
import pandas as pd

class URLExtractor:

    def extract(self, url, name):
        
        filepath = create_filepath(name)

        if name != "cines":
            r = requests.get(url)
            with open(filepath, 'wb') as f:
                f.write(r.content)
    
        return filepath



    




    
    