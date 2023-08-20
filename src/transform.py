from abc import abstractmethod
import pandas as pd
import io

class CinesData():
    def __init__(self, df_cines):
        self.df = df_cines


    def get_insights_table(self):
        cines = self.df
        cines['espacio_INCAA'] = cines['espacio_INCAA'].fillna(0)
        cines['espacio_INCAA'] = cines['espacio_INCAA'].replace(['si', 'SI'], '1')
        cines['espacio_INCAA'] = cines['espacio_INCAA'].astype('int64')
        cines_insights = cines.groupby("provincia")[["Pantallas", "Butacas", "espacio_INCAA"]].sum().reset_index()
        return cines_insights


class MergeData():
    
    def __init__(self, df, dfs_source):
        self.df = df
        self.sources = dfs_source
    
    def get_df(self):
        return self.df

    def get_count_by_category(self):
        size_by_category = self.df.groupby("categoría", as_index=False).size()
        return size_by_category
    
    def get_count_by_source(self):
        lst = list()
        for name, df in self.sources.items():
            lst.append({'source': name, 'count':df.size})
        
        return pd.DataFrame(lst)

    def get_count_by_province_category(self):
        return self.df.groupby(["provincia", "categoría"], as_index=False).size()
    
    



    
    