class Carrito:
    def __init__(self):
        self._items = []  # Lista de (producto, cantidad)

    def agregar_producto(self, producto, cantidad):
        self._items.append((producto, cantidad))

    def mostrar_resumen(self):
        print("\nResumen de compra:")
        total = 0
        for producto, cantidad in self._items:
            subtotal = producto.get_precio() * cantidad
            print(f"{cantidad} x {producto.get_nombre()} - ${subtotal:.3f}")
            total += subtotal
        print(f"Total a pagar: ${total:.3f}") #redondeo solo a tres decimales, no se si es correcto esto para guaranies
