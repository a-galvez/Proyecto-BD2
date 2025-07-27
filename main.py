from ETLs.etl_categoriaProducto import etl_categoriaProducto
from ETLs.etl_canalVenta import etl_canalVenta
from ETLs.etl_provincia import etl_provincia
from ETLs.etl_cliente import etl_cliente
from ETLs.etl_hechos import etl_hechos
from ETLs.etl_metodoEnvio import etl_metodoEnvio
from ETLs.etl_pais import etl_pais
from ETLs.etl_producto import etl_producto
from ETLs.etl_subcategoriaProducto import etl_subcategoriaProducto
from ETLs.etl_tiempo import etl_tiempo
from ETLs.etl_vendedor import etl_vendedor

from automatico import automatico

print("==== Proyecto Final Bases de Datos 2 - Grupo 1 =====")
print("Seleccione el modo para ejecutar el ETL:")
print("1. Automático")
print("2. Manual")

opcion = input("Ingrese su opción: ")

match opcion:
    case "1":
        print("Ejecutando ETL en modo automático...")
        automatico()
    case "2":
        print("Ejecutando ETL en modo manual...")
        # ejecutar_etl_manual()
    case _:
        print("Opción no válida")
