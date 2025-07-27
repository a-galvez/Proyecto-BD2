import pandas as pd
from conexion import conectar_bd
from transformaciones import transformar_mayusculas, transformar_minusculas


def etl_provincia():
    try:
        # Conexión a OLTP y OLAP
        engine_oltp = conectar_bd("AdventureWorks2022")
        engine_olap = conectar_bd("OLAP_AdventureWorks")

        # Consulta ingresada por el usuario
        consulta = input("-> Ingrese la consulta SQL para extraer las provincias:\n")

        # Extracción
        df = pd.read_sql(consulta, engine_oltp)

        # Carga solo nuevas registros
        df_existentes = pd.read_sql("SELECT IdProvincia FROM DimProvincia", engine_olap)
        nuevos = df[~df["IdProvincia"].isin(df_existentes["IdProvincia"])]

        # Carga
        nuevos.to_sql("DimProvincia", engine_olap, if_exists="append", index=False)
        print("---- ETL completado exitosamente para DimProvincia ----")

    except Exception as e:
        print("Error en el ETL: ", str(e))
