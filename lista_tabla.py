from nodo_tabla import Nodo_Tabla

class Lista_Tabla:
    def __init__(self):
        self.primero = None  # Inicio de la lista enlazada

    def insertar(self, tiempo, lineas):
        nuevo_nodo = Nodo_Tabla(tiempo, lineas)
        if not self.primero:
            self.primero = nuevo_nodo
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def imprimir_tabla(self):
        actual = self.primero
        while actual:
            print(f"Tiempo: {actual.tiempo}")
            for i, accion in enumerate(actual.lineas):
                print(f"Línea {i + 1}: {accion}")
            actual = actual.siguiente
