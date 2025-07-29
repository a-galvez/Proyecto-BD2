import pandas as pd
from conexion import conectar_bd
from transformaciones import (
    transformar_mayusculas,
)


def etl_canalVenta():
    try:
        # Conexión a OLTP y OLAP
        engine_oltp = conectar_bd("AdventureWorks2022")
        engine_olap = conectar_bd("OLAP_AdventureWorks")

        # Consulta ingresada por el usuario
        consulta = input(
            "-> Ingrese la consulta SQL para extraer los canales de venta: \n"
        )

        # Extracción
        df = pd.read_sql(consulta, engine_oltp)

        # Carga solo nuevas registros
        df_existentes = pd.read_sql("SELECT Canal FROM DimCanalVenta", engine_olap)
        nuevos = df[~df["Canal"].isin(df_existentes["Canal"])]

        # Carga
        nuevos.to_sql("DimCanalVenta", engine_olap, if_exists="append", index=False)
        print("---- ETL completado exitosamente para DimCanalVenta ----\n")

    except Exception as e:
        print("Error en el ETL de Canal de Venta: \n", str(e))
