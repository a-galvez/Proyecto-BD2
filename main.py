from ETLs import (
    etl_categoriaProducto,
    etl_canalVenta,
    etl_ciudad,
    etl_cliente,
    etl_hechos,
    etl_metodoEnvio,
    etl_pais,
    etl_producto,
    etl_subcategoriaProducto,
    etl_tiempo,
    etl_vendedor,
)

while True:
    print("=== ETL para la base de datos AdventureWorks2022 ===")
    opcion = input(
        "¿Qué tabla desea cargar?\n"
        " 1. Método de Envío\n"
        " 2. Ciudad\n"
        " 3. País\n"
        " 4. Cliente\n"
        " 5. Canal de Venta\n"
        " 6. Vendedor\n"
        " 7. Tiempo\n"
        " 8. Producto\n"
        " 9. Subcategoría de Producto\n"
        "10. Categoría de Producto\n"
        "11. Tabla de Hechos (Ventas)\n"
        "Seleccione una opción (1-11): "
    ).strip()

    match opcion:
        case "1":
            etl_metodoEnvio()
        case "2":
            etl_ciudad()
        case "3":
            etl_pais()
        case "4":
            etl_cliente()
        case "5":
            etl_canalVenta()
        case "6":
            etl_vendedor()
        case "7":
            etl_tiempo()
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
