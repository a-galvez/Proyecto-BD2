from ETLs.etl_categoriaProducto import etl_categoriaProducto

# from ETLs.etl_canalVenta import etl_canalVenta
# from ETLs.etl_ciudad import etl_ciudad
# from ETLs.etl_cliente import etl_cliente
from ETLs.etl_hechos import etl_hechos

# from ETLs.etl_metodoEnvio import etl_metodoEnvio
# from ETLs.etl_pais import etl_pais
from ETLs.etl_producto import etl_producto
from ETLs.etl_subcategoriaProducto import etl_subcategoriaProducto

# from ETLs.etl_tiempo import etl_tiempo
# from ETLs.etl_vendedor import etl_vendedor


while True:
    print("=== ETL para la base de datos AdventureWorks2022 ===")
    opcion = input(
        "¿Qué tabla desea cargar?\n"
        " 1. Método de Envío\n"  # Stelin
        " 2. Ciudad\n"  # Nohelia
        " 3. País\n"  # Nohelia
        " 4. Cliente\n"  # Stelin
        " 5. Canal de Venta\n"  # Stelin
        " 6. Vendedor\n"  # Stelin
        " 7. Tiempo\n"  # Stelin
        " 8. Producto\n"  # Aída
        " 9. Subcategoría de Producto\n"  # Aída
        "10. Categoría de Producto\n"  # Aída
        "11. Tabla de Hechos (Ventas)\n"  # Aída
        "Seleccione una opción (1-11): "
    ).strip()

    match opcion:
        case "1":
            # etl_metodoEnvio()
            print("Falta")
        case "2":
            # etl_ciudad()
            print("Falta")
        case "3":
            # etl_pais()
            print("Falta")
        case "4":
            # etl_cliente()
            print("Falta")
        case "5":
            # etl_canalVenta()
            print("Falta")
        case "6":
            # etl_vendedor()
            print("Falta")
        case "7":
            # etl_tiempo()
            print("Falta")
        case "8":
            etl_producto()
        case "9":
            etl_subcategoriaProducto()
        case "10":
            etl_categoriaProducto()
        case "11":
            etl_hechos()
        case _:
            print("Opción no válida.")

    continuar = input("¿Desea cargar otra tabla? (s/n): ").strip().lower()
    if continuar != "s":
        break
