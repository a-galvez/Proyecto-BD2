import pandas as pd
from conexion import conectar_bd


def etl_tiempo():

    try:
        # Conexión a OLTP y OLAP
        engine_oltp = conectar_bd("AdventureWorks2022")
        engine_olap = conectar_bd("OLAP_AdventureWorks")

        # Consulta ingresada por el usuario
        consulta = input(
            "-> Ingrese la consulta SQL para extraer las fechas únicas: \n"
        )

        # Extracción
        df = pd.read_sql(consulta, engine_oltp)

        # Carga solo nuevas registros
        df_existentes = pd.read_sql("SELECT IdTiempo FROM DimTiempo", engine_olap)
        nuevos = df[~df["IdTiempo"].isin(df_existentes["IdTiempo"])]

        # Carga
        nuevos.to_sql("DimTiempo", engine_olap, if_exists="append", index=False)
        print("---- ETL completado exitosamente para DimTiempo ----\n")

    except Exception as e:
        print("Error en el ETL: \n", str(e))
