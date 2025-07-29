import pandas as pd
from conexion import conectar_bd
from transformaciones import (
    transformar_mayusculas,
    transformar_minusculas,
    extraer_fecha,
)


def etl_categoriaProducto():
    try:
        # Conexión a OLTP y OLAP
        engine_oltp = conectar_bd("AdventureWorks2022")
        engine_olap = conectar_bd("OLAP_AdventureWorks")

        # Consulta ingresada por usuario
        consulta = input(
            "-> Ingrese la consulta SQL para extraer las categorías de productos:\n"
        )

        # Extracción
        df = pd.read_sql(consulta, engine_oltp)

        # Cargar solo nuevos registros
        df_existentes = pd.read_sql(
            "SELECT IdCategoria FROM DimCategoriaProducto", engine_olap
        )
        nuevos = df[~df["IdCategoria"].isin(df_existentes["IdCategoria"])]
        # Carga
        nuevos.to_sql(
            "DimCategoriaProducto", engine_olap, if_exists="append", index=False
        )
        print("---- ETL completado exitosamente para DimCategoriaProducto ----\n")

    except Exception as e:
        print("Error en el ETL: \n", str(e))
