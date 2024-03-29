
URL_MUSEOS = "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv"
URL_CINES = "https://datos.cultura.gob.ar/dataset/0560ef96-55ca-4026-b70a-d638e1541c05/resource/b8bf0459-16a5-430b-b8e1-4fb786572469/download/salas_cine.csv"
URL_BIBLIOTECAS = "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv"

# Detalles de la conexión a la base de datos
USER = "postgres"
PASSWORD = "123456"
HOST = "localhost"
PORT = "5432"
DATABASE_NAME = "DataAlkemyChallenge"

CONNECTION_STRING = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}"