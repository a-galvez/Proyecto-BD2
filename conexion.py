from sqlalchemy import create_engine


def conectar_bd(nombre_bd, servidor="localhost", usuario="sa", contraseña="1234"):
    cadena_conexion = f"mssql+pyodbc://{usuario}:{contraseña}@{servidor}/{nombre_bd}?driver=ODBC+Driver+17+for+SQL+Server"
    return create_engine(cadena_conexion)
