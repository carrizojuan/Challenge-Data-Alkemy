CREATE TABLE IF NOT EXISTS cine_insights
(
    provincia varchar(255) not null,
    pantallas integer,
    butacas integer,
    espacio_INCAA boolean
);

CREATE TABLE IF NOT EXISTS merge
(
    cod_localidad integer,
    id_provincia integer,
    id_departamento integer,
    "categoría" varchar(255),
    provincia varchar(255),
    localidad varchar(255),
    nombre varchar(255),
    domicilio varchar(255),
    "código postal" varchar(255),
    "número de teléfono" varchar(255),
    mail varchar(255),
    web varchar(255)
);

CREATE TABLE IF NOT EXISTS size_by_category
(
    "categoría" varchar(255),
    size integer
);

CREATE TABLE IF NOT EXISTS size_by_prov_cat
(
    provincia varchar(255),
    "categoría" varchar(255),
    size integer
);

CREATE TABLE IF NOT EXISTS size_by_source
(
    source varchar(255),
    count integer
)



