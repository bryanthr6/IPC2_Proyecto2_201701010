#nodo_posicion.py
class Nodo_Posicion:
    def __init__(self, linea, posicion):
        self.linea = linea  # Número de la línea de ensamblaje
        self.posicion = posicion  # Posición actual del brazo en esa línea
        self.siguiente = None  # Puntero al siguiente nodo
