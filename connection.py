from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.sql import text



def connect(user, password, host, port, database_name):

    connection_string = f"postgresql://{user}:{password}@{host}:{port}/{database_name}"

    # Definir los detalles de la conexión a la base de datos
    engine = create_engine(connection_string)

    # Abrir el archivo de script SQL y leer su contenido
    with open('create_tables.sql', 'r') as f:
        script = f.read()

    try:
        with engine.connect() as connection:
            connection.execute(text(script))
            connection.commit()
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
    
    return engine