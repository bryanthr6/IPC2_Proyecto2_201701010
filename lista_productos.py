#lista_productos.py
from nodo_producto import Nodo_Producto
from producto import Producto

class Lista_Productos:
    def __init__(self):
        self.primero = None

    def insertar(self, producto):
        if not self.primero:
            self.primero = Nodo_Producto(producto)
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = Nodo_Producto(producto)

    def imprimir(self):
        actual = self.primero
        while actual:
            print(f"Nombre: {actual.producto.nombre}")
            print(f"Elaboracion: {actual.producto.elaboracion}")
            actual = actual.siguiente
