# lista_acciones.py
from nodo_accion import Nodo_Accion

class Lista_Acciones:
    def __init__(self):
        self.primero = None  # Primer nodo de la lista enlazada

    def insertar(self, accion):
        # Crear un nuevo nodo de acción
        nuevo_nodo = Nodo_Accion(accion)

        # Si la lista está vacía, el nuevo nodo es el primero
        if self.primero is None:
            self.primero = nuevo_nodo
        else:
            # Recorrer hasta el final de la lista para insertar el nuevo nodo
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def recorrer(self):
        # Recorre la lista y devuelve las acciones en orden
        actual = self.primero
        while actual:
            yield actual.accion
            actual = actual.siguiente
