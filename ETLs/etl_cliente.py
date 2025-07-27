import pandas as pd
from conexion import conectar_bd
from transformaciones import (
    transformar_mayusculas,
    transformar_minusculas,
    extraer_fecha,
)


def etl_cliente():
    try:
        engine_oltp = conectar_bd("AdventureWorks2022")
        engine_olap = conectar_bd("OLAP_AdventureWorks")

        consulta = input("-> Ingrese la consulta SQL para extraer los clientes:\n")

        df = pd.read_sql(consulta, engine_oltp)

        df = transformar_mayusculas(df, "NombreCliente")

        df_existentes = pd.read_sql("SELECT IdCliente FROM DimCliente", engine_olap)
        nuevos = df[~df["IdCliente"].isin(df_existentes["IdCliente"])]

        nuevos.to_sql("DimCliente", engine_olap, if_exists="append", index=False)
        print("---- ETL completado exitosamente para DimCliente ----")

    except Exception as e:
        print("Error en el ETL: ", str(e))
