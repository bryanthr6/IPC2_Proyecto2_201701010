# nodo_segundo_accion.py
class Nodo_SegundoAccion:
    def __init__(self, segundo, linea, accion):
        self.segundo = segundo  # Segundo en que ocurre la acción
        self.linea = linea  # Línea de producción
        self.accion = accion  # Acción a realizar
        self.siguiente = None  # Puntero al siguiente nodo
