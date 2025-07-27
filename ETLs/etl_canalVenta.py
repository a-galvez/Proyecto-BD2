import pandas as pd
from conexion import conectar_bd
from transformaciones import (
    transformar_mayusculas,
)

def etl_canalVenta():
    try:
        engine_olap = conectar_bd("OLAP_AdventureWorks")
        canales_a_crear = [
            {'Canal': 'Online'},
            {'Canal': 'Tienda'}
        ]
        df_nuevos = pd.DataFrame(canales_a_crear)

        df_nuevos = transformar_mayusculas(df_nuevos, 'Canal')

        try:
            df_existentes = pd.read_sql("SELECT Canal FROM DimCanalVenta", engine_olap)
        except Exception:
            df_existentes = pd.DataFrame(columns=['Canal'])
        
        df_a_insertar = df_nuevos[~df_nuevos['Canal'].isin(df_existentes['Canal'])]

        if not df_a_insertar.empty:
            df_a_insertar.to_sql("DimCanalVenta", engine_olap, if_exists="append", index=False)
            print(f"ETL completado: Se insertaron {len(df_a_insertar)} nuevos canales.")
        else:
            print("ETL completado: No había nuevos canales para insertar.")

    except Exception as e:
        print("Error en el ETL de Canal de Venta:", str(e))
