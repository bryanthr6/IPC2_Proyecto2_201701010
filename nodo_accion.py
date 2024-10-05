class NodoAccion:
    def __init__(self, segundo, acciones):
        self.segundo = segundo
        self.acciones = acciones  # Este es el diccionario de acciones por línea
        self.siguiente = None