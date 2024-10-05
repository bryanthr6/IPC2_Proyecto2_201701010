# lista_productos_acumulados.py
from nodo_producto import Nodo_Producto
from producto import Producto

class Lista_Productos_Acumulados:
    def __init__(self):
        self.primero = None  # El primer nodo de la lista enlazada

    def insertar(self, producto):
        if not self.primero:
            self.primero = Nodo_Producto(producto)
        else:
            actual = self.primero
            while actual.siguiente:  # Ir hasta el último nodo
                actual = actual.siguiente
            actual.siguiente = Nodo_Producto(producto)  # Insertar al final de la lista

    def imprimir(self):
        actual = self.primero
        if not actual:
            print("No hay productos acumulados.")
            return
        while actual:
            print(f"Nombre: {actual.producto.nombre}")
            print(f"Elaboración: {actual.producto.elaboracion}")
            actual = actual.siguiente
