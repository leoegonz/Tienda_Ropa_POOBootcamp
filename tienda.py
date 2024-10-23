class Tienda:
    def __init__(self):
        self._productos = []  # Lista de productos disponibles

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def mostrar_productos(self):
        print("Productos disponibles en la tienda:")
        for i, producto in enumerate(self._productos, 1):
            print(f"{i}. ", end="")
            producto.mostrar_info()
            print("-" * 40) #son ---- para separar cada producto

    def obtener_producto(self, indice):
        if 0 <= indice < len(self._productos):
            return self._productos[indice]
        return None
