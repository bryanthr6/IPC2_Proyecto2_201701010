class NodoSegundoAccion:
    def __init__(self, segundo, linea, accion):
        self.segundo = segundo  # El número de segundo
        self.acciones = [(linea, accion)]  # Lista de acciones para ese segundo
        self.siguiente = None  # El siguiente nodo en la lista

    def agregar_accion(self, linea, accion):
        self.acciones.append((linea, accion))  # Agrega una nueva acción al segundo
