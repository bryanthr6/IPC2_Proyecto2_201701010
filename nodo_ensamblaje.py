from lista_componentes import ListaComponentes

class NodoLineaEnsamblaje:
    def __init__(self, numero_linea):
        self.numero_linea = numero_linea
        self.componentes = ListaComponentes()  # Lista enlazada de componentes
        self.posicion_brazo = 0  # Posición inicial del brazo en la línea
        self.siguiente = None  # Siguiente línea de ensamblaje
