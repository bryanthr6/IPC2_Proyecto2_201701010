class NodoComponente:
    def __init__(self, numero, tiempo_ensamblaje):
        self.numero = numero
        self.tiempo_ensamblaje = tiempo_ensamblaje
        self.siguiente = None  # Puntero al siguiente componente
