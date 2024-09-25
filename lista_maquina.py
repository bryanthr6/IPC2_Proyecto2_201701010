from maquina import Maquina

class NodoMaquina:
    def __init__(self, nombre_maquina):
        self.maquina = Maquina(nombre_maquina, 0)  # Inicialmente sin líneas
        self.siguiente = None

class ListaEnlazadaMaquinas:
    def __init__(self):
        self.cabeza = None

    def agregar_maquina(self, nombre_maquina):
        nueva_maquina = NodoMaquina(nombre_maquina)
        if self.cabeza is None:
            self.cabeza = nueva_maquina
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nueva_maquina
