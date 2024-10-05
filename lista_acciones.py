from nodo_accion import NodoAccion

class ListaAcciones:
    def __init__(self):
        self.primero = None

    def agregar_accion(self, segundo, linea, accion):
        """ Agrega o actualiza la acción de una línea en un segundo específico """
        nodo_actual = self.primero
        nodo_anterior = None

        # Buscar si ya existe un nodo para el segundo
        while nodo_actual is not None:
            if nodo_actual.segundo == segundo:
                # Actualizar la acción para la línea
                nodo_actual.acciones[linea] = accion
                return
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente

        # Si no se encontró un nodo para el segundo, creamos uno nuevo
        nuevo_nodo = NodoAccion(segundo, {linea: accion})

        if nodo_anterior is None:
            # Insertar como primer nodo si la lista está vacía
            self.primero = nuevo_nodo
        else:
            # Añadir al final de la lista
            nodo_anterior.siguiente = nuevo_nodo

    def obtener_acciones(self, segundo):
        """ Devuelve un diccionario con las acciones para un segundo específico, si existen """
        nodo_actual = self.primero
        while nodo_actual is not None:
            if nodo_actual.segundo == segundo:
                return nodo_actual.acciones  # Debería ser un objeto donde puedas buscar por línea
            nodo_actual = nodo_actual.siguiente
        return None  # Si no se encontraron acciones para ese segundo

