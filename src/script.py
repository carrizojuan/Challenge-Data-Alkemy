from sqlalchemy import create_engine, text

# Definir los detalles de la conexión a la base de datos
user = "postgres"
password = "Carry_43346"
host = "127.0.0.1"
port = "5432"
database_name = "AlkemyChallenge"

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


