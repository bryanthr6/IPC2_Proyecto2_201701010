from nodo_componente import NodoComponente

class ListaComponentes:
    def __init__(self):
        self.cabeza = None  # Primer componente de la lista

    def agregar_componente(self, numero, tiempo_ensamblaje):
        nuevo_componente = NodoComponente(numero, tiempo_ensamblaje)
        if self.cabeza is None:
            self.cabeza = nuevo_componente
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_componente  # Enlaza el nuevo componente al final
    
    def obtener_componente(self, numero):
        # Devuelve el nodo del componente con el número indicado
        actual = self.cabeza
        while actual is not None:
            if actual.numero == numero:
                return actual
            actual = actual.siguiente
        return None
