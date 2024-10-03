# nodo_accion.py
class Nodo_Accion:
    def __init__(self, accion=None):
        self.accion = accion  # El texto de la acción
        self.siguiente = None  # Puntero al siguiente nodo
