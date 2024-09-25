from nodo_ensamblaje import NodoLineaEnsamblaje

class ListaLineasEnsamblaje:
    def __init__(self):
        self.cabeza = None  # Primera línea de ensamblaje

    def agregar_linea(self, numero_linea):
        nueva_linea = NodoLineaEnsamblaje(numero_linea)
        if self.cabeza is None:
            self.cabeza = nueva_linea
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nueva_linea
    
    def obtener_linea(self, numero_linea):
        # Devuelve el nodo de la línea de ensamblaje con el número indicado
        actual = self.cabeza
        while actual is not None:
            if actual.numero_linea == numero_linea:
                return actual
            actual = actual.siguiente
        return None
