# Tienda_Ropa_POOBootcamp
Este proyecto es una simulación muy basica de una tienda en línea, donde el usuario puede seleccionar productos de diferentes tipos; En este caso solo camisas, pantalones y zapatos.
El programa implementa los pilares de la Programación Orientada a Objetos (POO) que son: encapsulamiento, herencia, polimorfismo y abstracción.


## *Características de las POO y el proyecto*
- **Encapsulamiento**: Los atributos como el nombre, precio, talla y tipo de tela están encapsulados y se accede a ellos mediante métodos. Osea los atributos de las clases están protegidos y solo accesibles a través de getters y setters.
- **Herencia**: Las clases de `ropa` heredan de una clase base `Producto`, y las clases más específicas como `Camisa`, `Pantalon` y `Zapato` heredan de `Ropa`.
- **Polimorfismo**: El método `mostrar_info()` es polimórfico, ya que se sobrescribe en cada clase para mostrar la información adecuada según el tipo de producto.
- **Abstracción**: El proceso de compra está abstraído, permitiendo al usuario interactuar de manera sencilla sin ver los detalles internos del programa.


## *Ejecución:*
- Ejecute el programa desde la terminal, el programa que debes ejecutar es: main.py
- Sigue las instrucciones que se muestran en la terminal para seleccionar productos y realizar compras.


## *Estructura del Proyecto:*
- **main.py**: Ejecuta el programa principal.
- **producto.py**: Contiene la clase base Producto.
- **ropa.py**: Contiene la clase Ropa y las clases derivadas como Camisa, Pantalon, y Zapato.
- **tienda.py**: Contiene la clase Tienda que maneja el inventario.
- **carrito.py**: Contiene la clase Carrito, donde se almacenan los productos seleccionados.


## Contribuciones
*Las contribuciones son bienvenidas.*