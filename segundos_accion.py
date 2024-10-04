# segundos_accion.py
class NodoAccion:
    def __init__(self, segundo, linea, accion):
        self.segundo = segundo
        self.linea = linea
        self.accion = accion
        self.siguiente = None

class Lista_SegundosAccion:
    def __init__(self):
        self.primero = None

    def insertar(self, segundo, linea, accion):
        nuevo_nodo = NodoAccion(segundo, linea, accion)
        if self.primero is None:
            self.primero = nuevo_nodo
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def obtener_acciones(self):
        acciones = []
        actual = self.primero
        while actual:
            acciones.append((actual.segundo, actual.linea, actual.accion))
            actual = actual.siguiente
        return acciones
