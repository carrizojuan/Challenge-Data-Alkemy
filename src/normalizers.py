class Normalizer:
    def __init__(self, df):
        self.column_norm_names = ["cod_localidad", "id_provincia", "id_departamento","categoría",
              "provincia","localidad","nombre","domicilio","código postal","número de teléfono","mail","web"] 
        self.df = df

    def normalize(self):
        pass

class MuseoNormalizer(Normalizer):
    def __init__(self, df):
        super().__init__(df)
        self.column_rename = {
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

    def normalize(self):
        df_museo = self.df
        df_museo.rename(columns=self.column_rename, inplace=True)
        df_museo = df_museo[self.column_norm_names]
        return df_museo
     

class CineNormalizer(Normalizer):

    def __init__(self, df):
        super().__init__(df)
        self.column_rename = {
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
            'Nombre':'nombre'}
    
    def normalize(self):
        df_cine = self.df
        df_cine.rename(columns=self.column_rename, inplace=True)
        df_cine = df_cine[self.column_norm_names]
        df_cine['código postal'] = df_cine['código postal'].astype(object)
        return df_cine


class BibliotecaNormalizer(Normalizer):

    def __init__(self, df):
        super().__init__(df)
        self.column_rename = {
            'categoria':'categoría',
            'cp':'código postal',
            'telefono':'número de teléfono'}
    
    def normalize(self):
        df_biblioteca = self.df
        df_biblioteca.rename(columns=self.column_rename, inplace=True)
        df_biblioteca = df_biblioteca[self.column_norm_names]
        return df_biblioteca
    


