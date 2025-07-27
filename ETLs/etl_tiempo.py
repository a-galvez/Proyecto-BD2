import pandas as pd
from conexion import conectar_bd
from transformaciones import extraer_fecha
import locale

try:
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
except locale.Error:
    locale.setlocale(locale.LC_TIME, '')

def etl_tiempo():
    try:
        engine_oltp = conectar_bd("AdventureWorks2022")
        engine_olap = conectar_bd("OLAP_AdventureWorks")

        consulta = input("Ingrese la consulta SQL para extraer las fechas únicas:\n")
        df = pd.read_sql(consulta, engine_oltp)
        
        df['Fecha'] = pd.to_datetime(df['Fecha'])
        df['Dia'] = extraer_fecha(df, 'Fecha', 'dia')
        df['Mes'] = extraer_fecha(df, 'Fecha', 'mes')
        df['Anio'] = extraer_fecha(df, 'Fecha', 'anio')
        df['NombreMes'] = df['Fecha'].dt.strftime('%B').str.capitalize()
        df['Trimestre'] = df['Fecha'].dt.quarter
        
        # Leemos solo la fecha de los registros existentes para comparar
        df_existentes = pd.read_sql("SELECT Fecha FROM DimTiempo", engine_olap)
        df_existentes['Fecha'] = pd.to_datetime(df_existentes['Fecha'])

        # Comparamos por la columna 'Fecha' para encontrar los nuevos
        nuevos = df[~df["Fecha"].isin(df_existentes["Fecha"])]
        
        # ¡IMPORTANTE! Aquí ya no creamos ni enviamos 'IdTiempo'.
        # SQL Server lo generará automáticamente al insertar.

        nuevos.to_sql("DimTiempo", engine_olap, if_exists="append", index=False)
        print("ETL completado exitosamente para DimTiempo")

    except Exception as e:
        print("Error en el ETL:", str(e))
