import pandas as pd
from conexion import conectar_bd
from transformaciones import (
    transformar_mayusculas,
    transformar_minusculas,
    extraer_fecha,
)


def etl_vendedor():
    try:
        engine_oltp = conectar_bd("AdventureWorks2022")
        engine_olap = conectar_bd("OLAP_AdventureWorks")

        consulta = input("-> Ingrese la consulta SQL para extraer los vendedores:\n")

        df = pd.read_sql(consulta, engine_oltp)

        df = transformar_mayusculas(df, "NombreVendedor")

        df_existentes = pd.read_sql("SELECT IdVendedor FROM DimVendedor", engine_olap)
        nuevos = df[~df["IdVendedor"].isin(df_existentes["IdVendedor"])]

        nuevos.to_sql("DimVendedor", engine_olap, if_exists="append", index=False)
        print("---- ETL completado exitosamente para DimVendedor ----")

    except Exception as e:
        print("Error en el ETL: ", str(e))
