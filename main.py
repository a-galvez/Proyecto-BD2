from ETLs.etl_producto import etl_producto
from ETLs.etl_categoriaProducto import etl_categoriaProducto

print("=== ETL del proyecto Data Warehouse ===")
opcion = (
    input("¿Qué tabla desea cargar? (producto/cliente/fact/categoria): ")
    .strip()
    .lower()
)

if opcion == "producto":
    etl_producto()
elif opcion == "cliente":
    # etl_cliente()
    pass
elif opcion == "fact":
    # etl_fact_ventas()
    pass
elif opcion == "categoria":
    etl_categoriaProducto()
    pass
else:
    print("⚠️ Opción no válida.")
