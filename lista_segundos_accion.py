# lista_segundos_accion.py
from nodo_segundo_accion import Nodo_SegundoAccion

class Lista_SegundosAccion:
    def __init__(self):
        self.primero = None

    def insertar(self, segundo, linea, accion):
        nuevo_nodo = Nodo_SegundoAccion(segundo, linea, accion)
        if self.primero is None:
            self.primero = nuevo_nodo
        else:
            actual = self.primero
            # Insertar al final de la lista
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def obtener_acciones_por_segundo(self, segundo):
        actual = self.primero
        acciones = []
        while actual:
            if actual.segundo == segundo:
                acciones.append((actual.linea, actual.accion))
            actual = actual.siguiente
        return acciones  # Retornar todas las acciones para ese segundo

    def imprimir(self):
        actual = self.primero
        while actual:
            print(f"Segundo: {actual.segundo}, Línea: {actual.linea}, Acción: {actual.accion}")
            actual = actual.siguiente
