from sqlalchemy import create_engine, text

# Definir los detalles de la conexión a la base de datos
user = "postgres"
password = "123456"
host = "localhost"
port = "5432"
database_name = "DataAlkemyChallenge"

connection_string = f"postgresql://{user}:{password}@{host}:{port}/{database_name}"

# Definir los detalles de la conexión a la base de datos
engine = create_engine(connection_string)

connection = engine.connect()

# Abrir el archivo de script SQL y leer su contenido
with open('create_tables.sql', 'r') as f:
    script = f.read()

# intenta eliminar la tabla 'prueba'
try:
    connection.execute(text(script))
    connection.commit()
except Exception as e:
    print(e)
    # si se produce algún error, deshace los cambios realizados en la transacción
    connection.rollback()


