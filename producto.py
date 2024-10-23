class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre 
        self._precio = precio

    # Getters
    def get_nombre(self):
        return self._nombre

    def get_precio(self):
        return self._precio

    # Setters
    def set_precio(self, nuevo_precio):
        self._precio = nuevo_precio

    def mostrar_info(self):
        print(f"Producto: {self._nombre}, Precio: ${self._precio:.3f}")
