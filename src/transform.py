from abc import abstractmethod
import pandas as pd
import io

def merge_dfs(paths, merge_path):

    columns_norm_names=["cod_localidad", "id_provincia", "id_departamento","categoría",
              "provincia","localidad","nombre","domicilio","código postal","número de teléfono","mail","web"]
    dfs = []
    sources = {}
    for name,path in paths.items():
        df = pd.read_csv(path)
        sources[name] = df
        dfs.append(rename_columns(df,name, columns_norm_names))
    
    merge_dfs = pd.concat(dfs, axis=0)
    merge_dfs.to_csv(merge_path, index=False)
    merge_data = MergeData(merge_dfs)
    merge_data.setSources(sources)

    return merge_data
    

def getCineInsights(path):
    cines = pd.read_csv(path)
    cines['espacio_INCAA'] = cines['espacio_INCAA'].fillna(0)
    cines['espacio_INCAA'] = cines['espacio_INCAA'].replace(['si', 'SI'], '1')
    cines['espacio_INCAA'] = cines['espacio_INCAA'].astype('int64')
    cines_insights = cines.groupby("Provincia")["Pantallas", "Butacas", "espacio_INCAA"].sum().reset_index()
    return cines_insights



def rename_columns(df, name, columns_norm_names):
    
    if name == "museos":
        column_rename = {
            'Cod_Loc':'cod_localidad',
            'IdProvincia':'id_provincia',
            'IdDepartamento':'id_departamento',
            'categoria':'categoría',
            'direccion':'domicilio',
            'CP':'código postal',
            'telefono':'número de teléfono',
            'Mail':'mail',
            'Web':'web'
        }
    elif name == "bibliotecas":
        column_rename = {
            'Cod_Loc':'cod_localidad',
            'IdProvincia':'id_provincia',
            'IdDepartamento':'id_departamento',
            'Categoría':'categoría',
            'Domicilio':'domicilio',
            'CP':'código postal',
            'Teléfono':'número de teléfono',
            'Mail':'mail',
            'Web':'web',
            'Provincia':'provincia',
            'Localidad':'localidad',
            'Nombre':'nombre',
        }
    elif name == "cines":
        column_rename = {
            'Cod_Loc':'cod_localidad',
            'IdProvincia':'id_provincia',
            'IdDepartamento':'id_departamento',
            'Categoría':'categoría',
            'Dirección':'domicilio',
            'CP':'código postal',
            'Teléfono':'número de teléfono',
            'Mail':'mail',
            'Web':'web',
            'Provincia':'provincia',
            'Localidad':'localidad',
            'Nombre':'nombre',   
        }

    df.rename(columns=column_rename, inplace=True)
    return df[columns_norm_names]


class MergeData():
    
    def __init__(self, merge_df):
        self.merge_df = merge_df
    
    def getDF(self):
        return self.merge_df

    def setSources(self,sources):
        self.sources = sources

    def getSizeByCategory(self):
        size_by_category = self.merge_df.groupby("categoría", as_index=False).size()
        return size_by_category
    
    def getSizeBySource(self):
        #dfs = {'museos':museos, 'cines':cines, 'bibliotecas':bibliotecas}
        lst = list()
        for name, df in self.sources.items():
            lst.append({'source': name, 'count':df.size})
        size_by_source = pd.DataFrame(lst)
        return size_by_source

    def getSizeByProvinceCategory(self):
        size_by_prov_cat = self.merge_df.groupby(["provincia", "categoría"], as_index=False).size()
        return size_by_prov_cat
    
    



    
    