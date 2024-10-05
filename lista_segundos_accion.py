from nodo_segundos_accion import NodoSegundoAccion

class ListaSegundosAccion:
    def __init__(self):
        self.primero = None  # Nodo inicial de la lista

    def agregar_segundo(self, segundo, linea, accion):
        # Si la lista está vacía, agregamos el primer nodo
        if not self.primero:
            self.primero = NodoSegundoAccion(segundo, linea, accion)
        else:
            actual = self.primero
            # Buscamos el segundo si ya existe
            while actual:
                if actual.segundo == segundo:
                    actual.agregar_accion(linea, accion)
                    return
                if not actual.siguiente:  # Si llegamos al final, lo añadimos
                    break
                actual = actual.siguiente
            actual.siguiente = NodoSegundoAccion(segundo, linea, accion)

    def obtener_acciones(self, segundo):
        actual = self.primero
        while actual:
            if actual.segundo == segundo:
                return actual.acciones
            actual = actual.siguiente
        return None  # No se encontró el segundo
