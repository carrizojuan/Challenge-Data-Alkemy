from sqlalchemy import create_engine
from datetime import datetime

# Definir los detalles de la conexión a la base de datos
user = "postgres"
password = "123456"
host = "localhost"
port = "5432"
database_name = "DataAlkemyChallenge"

connection_string = f"postgresql://{user}:{password}@{host}:{port}/{database_name}"

# Definir los detalles de la conexión a la base de datos
engine = create_engine(connection_string)


class BaseLoader:

    def load_table(self, df):
        df["fecha_carga"] = datetime.now()
        df.to_sql(self.table_name, con=engine, index=False, if_exists="replace")

class MergeDataLoader(BaseLoader):

    table_name = "merge_table"

    def load_table(self, df):
        
        return super().load_table(df)

class SizeByCategoryLoader(BaseLoader):
    table_name = "size_by_category"

    def load_table(self, df):
        return super().load_table(df)

class SizeByProvCatLoader(BaseLoader):
    table_name = "size_by_prov_cat"

    def load_table(self, df):
        return super().load_table(df)
    
class SizeBySourceLoader(BaseLoader):
    table_name = "size_by_source"

    def load_table(self, df):
        return super().load_table(df)
    
class CineInsightsLoader(BaseLoader):
    table_name = "cine_insights"

    def load_table(self, df):
        return super().load_table(df)