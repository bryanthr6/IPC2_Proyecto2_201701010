# lista_historial.py
from nodo_historial import Nodo_Historial
from lista_acciones import Lista_Acciones

class Lista_Historial:
    def __init__(self):
        self.primero = None  # El primer nodo de la lista enlazada

    def insertar(self, accion):
        # Crea un nuevo nodo con la acción
        nuevo_nodo = Nodo_Historial(accion)

        # Si la lista está vacía, el nuevo nodo es el primero
        if self.primero is None:
            self.primero = nuevo_nodo
        else:
            # Recorre hasta el final de la lista para agregar el nuevo nodo
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def obtener_historial(self):
        # Crear una lista enlazada para almacenar el historial de acciones
        lista_acciones = Lista_Acciones()
        
        # Recorrer la lista de historial y pasar cada acción a la lista de acciones
        actual = self.primero
        while actual:
            lista_acciones.insertar(actual.accion)
            actual = actual.siguiente
        
        # Retornar la lista enlazada de acciones
        return lista_acciones.recorrer()  # Devuelve un generador con las acciones
