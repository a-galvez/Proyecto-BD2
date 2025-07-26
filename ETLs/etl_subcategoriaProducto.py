import pandas as pd
from conexion import conectar_bd
from transformaciones import (
    transformar_mayusculas,
    transformar_minusculas,
    extraer_fecha,
)


def etl_subcategoriaProducto():
    try:
        # Conexión a OLTP y OLAP
        engine_oltp = conectar_bd("AdventureWorks2022")
        engine_olap = conectar_bd("OLAP_AdventureWorks")

        # Consulta ingresada por usuario
        consulta = input(
            "Ingrese la consulta SQL para extraer las subcategorias de productos:\n"
        )

        # Extracción
        df = pd.read_sql(consulta, engine_oltp)

        # Cargar solo nuevos registros
        df_existentes = pd.read_sql(
            "SELECT IdSubcategoria FROM DimSubcategoriaProducto", engine_olap
        )
        nuevos = df[~df["IdSubcategoria"].isin(df_existentes["IdSubcategoria"])]

        # Carga
        nuevos.to_sql(
            "DimSubcategoriaProducto", engine_olap, if_exists="append", index=False
        )
        print("ETL completado exitosamente para DimSubcategoriaProducto")

    except Exception as e:
        print("Error en el ETL:", str(e))
