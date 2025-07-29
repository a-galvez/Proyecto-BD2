import pandas as pd
from conexion import conectar_bd
from transformaciones import (
    transformar_mayusculas,
    transformar_minusculas,
    extraer_fecha,
)


def etl_metodoEnvio():
    try:

        engine_oltp = conectar_bd("AdventureWorks2022")
        engine_olap = conectar_bd("OLAP_AdventureWorks")

        consulta = input(
            "-> Ingrese la consulta SQL para extraer los métodos de envío: \n"
        )

        df = pd.read_sql(consulta, engine_oltp)

        df = transformar_mayusculas(df, "NombreMetodo")

        df_existentes = pd.read_sql(
            "SELECT IdMetodoEnvio FROM DimMetodoEnvio", engine_olap
        )
        nuevos = df[~df["IdMetodoEnvio"].isin(df_existentes["IdMetodoEnvio"])]

        # Carga
        nuevos.to_sql("DimMetodoEnvio", engine_olap, if_exists="append", index=False)
        print("---- ETL completado exitosamente para DimMetodoEnvio ----\n")

    except Exception as e:
        print("Error en el ETL: \n", str(e))
