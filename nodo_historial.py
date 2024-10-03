# nodo_historial.py
class Nodo_Historial:
    def __init__(self, accion=None):
        self.accion = accion  # La acción o mensaje que queremos almacenar
        self.siguiente = None  # Puntero al siguiente nodo
