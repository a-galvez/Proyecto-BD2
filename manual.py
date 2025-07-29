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

# Variables de estado
dependencias_ejecutadas = False
sin_dependencias_ejecutadas = False


def manual():
    global dependencias_ejecutadas, sin_dependencias_ejecutadas

    while True:
        print("\n-> ¿Qué ETL desea ejecutar primero?")
        print("1. ETLs de tablas con dependencias")
        print("2. ETLs de tablas sin dependencias")
        if dependencias_ejecutadas and sin_dependencias_ejecutadas:
            print("3. Ejecutar ETL de tabla de hechos")
        print("0. Salir\n")

        opcion = input("Ingrese su opción: ")

        match opcion:
            case "1":
                tablasConDependencias()
                dependencias_ejecutadas = True

            case "2":
                tablasSinDependencias()
                sin_dependencias_ejecutadas = True

            case "3" if dependencias_ejecutadas and sin_dependencias_ejecutadas:
                print("---- Ejecutando el ETL de la tabla de hechos ----\n")
                etl_hechos()

            case "0":
                print("Saliendo...")
                break

            case _:
                print("Opción no válida.")


def tablasConDependencias():
    print("\nEscoja qué ETLs de tablas con dependencias ejecutar primero:")
    print("1. Tabla DimPais -> Tabla DimProvincia -> Tabla DimCliente")
    print(
        "2. Tabla DimCategoríaProducto -> Tabla DimSubcategoríaProducto -> Tabla DimProducto\n"
    )

    opcion1 = input("Ingrese su opción: \n")

    match opcion1:
        case "1":
            cargarUbicaciones()
            print(
                "---- Se ejecutarán los ETLs de DimCategoríaProducto -> DimSubcategoríaProducto -> DimProducto ----\n"
            )
            cargarCategorias()

        case "2":
            cargarCategorias()
            print(
                "---- Se ejecutarán los ETLs de DimPais -> DimProvincia -> DimCliente ----\n"
            )
            cargarUbicaciones()

        case _:
            print("Opción no válida.")


def cargarUbicaciones():
    print("---- Ejecutando el ETL de la tabla DimPais -----\n")
    etl_pais()
    print("---- Ejecutando el ETL de la tabla DimProvincia ----\n")
    etl_provincia()
    print("---- Ejecutando el ETL de la tabla DimCliente ----\n")
    etl_cliente()


def cargarCategorias():
    print("---- Ejecutando el ETL de la tabla DimCategoriaProducto ----\n")
    etl_categoriaProducto()
    print("---- Ejecutando el ETL de la tabla DimSubcategoriaProducto ----\n")
    etl_subcategoriaProducto()
    print("---- Ejecutando el ETL de la tabla DimProducto ----\n")
    etl_producto()


def tablasSinDependencias():
    tablas_etl = {
        "1": ("DimCanalVenta", etl_canalVenta),
        "2": ("DimMétodoEnvío", etl_metodoEnvio),
        "3": ("DimTiempo", etl_tiempo),
        "4": ("DimVendedor", etl_vendedor),
    }

    etlEjecutado = set()

    while len(etlEjecutado) < len(tablas_etl):
        print("\nEscoja qué ETL desea ejecutar:")
        for clave, (nombre, _) in tablas_etl.items():
            if clave not in etlEjecutado:
                print(f"{clave}. Tabla {nombre}")
        print("0. Volver al menú principal\n")

        opcion = input("Ingrese su opción: ")

        if opcion == "0":
            break
        elif opcion in tablas_etl and opcion not in etlEjecutado:
            nombre, funcion = tablas_etl[opcion]
            print(f"---- Ejecutando el ETL de la tabla {nombre} ----\n")
            funcion()
            etlEjecutado.add(opcion)
        elif opcion in etlEjecutado:
            print("Esa tabla ya fue ejecutada.")
        else:
            print("Opción no válida.")

    if len(etlEjecutado) == len(tablas_etl):
        print("\nTodas las tablas sin dependencias han sido ejecutadas.")
