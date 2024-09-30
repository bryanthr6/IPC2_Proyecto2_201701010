from nodo_posicion import Nodo_Posicion

class Lista_Posicion:
    def __init__(self):
        self.primero = None  # Inicio de la lista enlazada

    def insertar_o_actualizar(self, linea, nueva_posicion):
        # Buscar si ya existe una posición para esta línea
        actual = self.primero
        while actual:
            if actual.linea == linea:
                actual.posicion = nueva_posicion  # Actualizar la posición si ya existe
                return
            actual = actual.siguiente
        
        # Si no se encuentra la línea, insertar una nueva posición
        nuevo_nodo = Nodo_Posicion(linea, nueva_posicion)
        nuevo_nodo.siguiente = self.primero  # Insertar al inicio de la lista
        self.primero = nuevo_nodo

    def obtener_posicion(self, linea):
        # Buscar la posición actual del brazo en la línea dada
        actual = self.primero
        while actual:
            if actual.linea == linea:
                return actual.posicion
            actual = actual.siguiente
        return 0  # Si no se encuentra, se asume que el brazo está en la posición inicial (0)
