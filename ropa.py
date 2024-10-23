from producto import Producto

class Ropa(Producto):
    def __init__(self, nombre, precio, talla, tipo_tela):
        super().__init__(nombre, precio)
        self._talla = talla
        self._tipo_tela = tipo_tela

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self._talla}, Tipo de Tela: {self._tipo_tela}")

class Camisa(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela, manga_larga):
        super().__init__(nombre, precio, talla, tipo_tela)
        self._manga_larga = manga_larga

    def mostrar_info(self):
        super().mostrar_info()
        if self._manga_larga:
            print("Tipo de manga: Manga larga")
        else:
            print("Tipo de manga: Manga corta")


class Pantalon(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela, tipo_corte):
        super().__init__(nombre, precio, talla, tipo_tela)
        self._tipo_corte = tipo_corte

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Tipo de corte: {self._tipo_corte}")

class Zapato(Ropa):
    def __init__(self, nombre, precio, talla, material):
        super().__init__(nombre, precio, talla, tipo_tela=None)  # El zapato puede no tener tipo de tela
        self._material = material

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Material: {self._material}")

