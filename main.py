from tienda import Tienda
from carrito import Carrito
from ropa import Camisa, Pantalon, Zapato

def realizar_compra(tienda):
    carrito = Carrito()

    while True:
        tienda.mostrar_productos()

        try:
            opcion = int(input("Selecciona el número del producto disponible que deseas comprar (Ingrese 0 para salir/terminar compra): "))
            if opcion == 0:
                break

            cantidad = int(input("¿Cuántas unidades deseas comprar?: "))
            producto = tienda.obtener_producto(opcion - 1)

            if producto:
                carrito.agregar_producto(producto, cantidad)
            else:
                print("Producto no válido.")
        
        except (ValueError, IndexError):
            print("Opción inválida, intenta de nuevo.")

    carrito.mostrar_resumen()

if __name__ == "__main__":
    tienda = Tienda()

    # Agregar productos a la tienda
    tienda.agregar_producto(Camisa("Camisa Formal", 105.000, "M", "Algodón", True)) #al poner true digo que es manga larga, si pongo false es manga corta
    tienda.agregar_producto(Pantalon("Jeans", 70.000, "L", "Denim", "Mom"))
    tienda.agregar_producto(Pantalon("Jeans", 70.000, "M", "Denim", "Mom"))
    tienda.agregar_producto(Zapato("Zapato Deportivo", 600.000, 42, "Cuero"))

    # Procesar la compra del usuario
    realizar_compra(tienda)

