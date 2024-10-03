class Nodo_Tabla:
    def __init__(self, tiempo, lineas):
        self.tiempo = tiempo  # Tiempo del ensamblaje
        self.lineas = lineas  # Lista enlazada que representará el estado de cada línea de ensamblaje
        self.siguiente = None  # Puntero al siguiente nodo
