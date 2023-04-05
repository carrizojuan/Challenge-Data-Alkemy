CREATE TABLE IF NOT EXISTS cine_insights
(
    "Provincia" text COLLATE pg_catalog."default",
    "Pantallas" bigint,
    "Butacas" bigint,
    "espacio_INCAA" bigint
);

CREATE TABLE IF NOT EXISTS merge_table
(
    cod_localidad bigint,
    id_provincia bigint,
    id_departamento bigint,
    "categoría" text COLLATE pg_catalog."default",
    provincia text COLLATE pg_catalog."default",
    localidad text COLLATE pg_catalog."default",
    nombre text COLLATE pg_catalog."default",
    domicilio text COLLATE pg_catalog."default",
    "código postal" text COLLATE pg_catalog."default",
    "número de teléfono" text COLLATE pg_catalog."default",
    mail text COLLATE pg_catalog."default",
    web text COLLATE pg_catalog."default"
);

CREATE TABLE IF NOT EXISTS size_by_category
(
    "categoría" text COLLATE pg_catalog."default",
    size bigint
);

CREATE TABLE IF NOT EXISTS size_by_prov_cat
(
    provincia text COLLATE pg_catalog."default",
    "categoría" text COLLATE pg_catalog."default",
    size bigint
);

CREATE TABLE IF NOT EXISTS size_by_source
(
    source text COLLATE pg_catalog."default",
    count integer
)



