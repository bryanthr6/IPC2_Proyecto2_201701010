
from lista_productos import Lista_Productos

class Maquina:
    def __init__(self, nombre, lineas, componentes, tiempo_ensamblaje, lista_productos):
        self.nombre = nombre
        self.lineas = lineas
        self.componentes = componentes
        self.tiempo_ensamblaje = tiempo_ensamblaje
        self.lista_productos = lista_productos  # Asignar directamente la lista de productos ya creada
