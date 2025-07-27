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


def automatico():
    print("---- Ejecutando el ETL de la tabla DimPais -----")
    etl_pais()
    print("---- Ejecutando el ETL de la tabla DimCiudad ----")
    etl_provincia()
    print("---- Ejecutando el ETL de la tabla DimCliente ----")
    etl_cliente()
    print("---- Ejecutando el ETL de la tabla DimCategoriaProducto ----")
    etl_categoriaProducto()
    print("---- Ejecutando el ETL de la tabla DimSubcategoriaProducto ----")
    etl_subcategoriaProducto()
    print("---- Ejecutando el ETL de la tabla DimProducto ----")
    etl_producto()
    print("---- Ejecutando el ETL de la tabla DimCanalVenta ----")
    etl_canalVenta()
    print("---- Ejecutando el ETL de la tabla DimMetodoEnvio ----")
    etl_metodoEnvio()
    print("---- Ejecutando el ETL de la tabla DimTiempo ----")
    etl_tiempo()
    print("---- Ejecutando el ETL de la tabla DimVendedor ----")
    etl_vendedor()
    print("---- Ejecutando el ETL de la tabla de Hechos ----")
    etl_hechos()
    print("---- Se ejecutaron todos los ETLs ----")
