import os
from datetime import datetime

def create_filepath(name):
    
    #Obtencion fecha actual
    today_date = datetime.now()

    #Obtencion mes y dia actual
    year_month = today_date.strftime('%Y-%B')

    # Crear el directorio "data" si no existe
    os.makedirs("data", exist_ok=True)

    folder = os.path.join("data", name, year_month)
    os.makedirs(folder, exist_ok=True)

    filename = f"{name}-{today_date.strftime('%d-%m-%Y')}.csv"

    filepath = os.path.join(folder, filename)
    
    return filepath

