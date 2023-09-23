from sqlalchemy import create_engine, text
import settings

connection_string = settings.CONNECTION_STRING
engine = create_engine(connection_string)

def create_tables():
    
    print("***********"*1000, engine)
    try:
        connection = engine.connect()
    except Exception as e:
        print(e)
    print("+"*1000)

    with open("scripts/create_tables.sql", "r") as f:
        query = text(f.read())

    
    try:
        connection.execute(query)
        connection.commit()
    except Exception as e:
        print(e)
        # si se produce algún error, deshace los cambios realizados en la transacción
        connection.rollback()


if __name__ == "__main__":
    create_tables()