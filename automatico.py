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


def ejecutar_etl(nombre_tabla, funcion_etl):
    print(f"---- Ejecutando el ETL de la tabla {nombre_tabla} ----\n")
    try:
        funcion_etl()
        print(f"ETL de {nombre_tabla} ejecutado correctamente.\n")
    except Exception as e:
        print("\n")


def automatico():
    ejecutar_etl("DimPais", etl_pais)
    ejecutar_etl("DimCiudad", etl_provincia)
    ejecutar_etl("DimCliente", etl_cliente)
    ejecutar_etl("DimCategoriaProducto", etl_categoriaProducto)
    ejecutar_etl("DimSubcategoriaProducto", etl_subcategoriaProducto)
    ejecutar_etl("DimProducto", etl_producto)
    ejecutar_etl("DimCanalVenta", etl_canalVenta)
    ejecutar_etl("DimMetodoEnvio", etl_metodoEnvio)
    ejecutar_etl("DimTiempo", etl_tiempo)
    ejecutar_etl("DimVendedor", etl_vendedor)
    ejecutar_etl("Tabla de Hechos", etl_hechos)

    print("---- Finalizó la ejecución automática de los ETLs ----\n")
