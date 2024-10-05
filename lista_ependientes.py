class NodoEP:
    def __init__(self, linea, componente, tiempo_inicio, tiempo_ensamblar):
        self.linea = linea
        self.componente = componente
        self.tiempo_inicio = tiempo_inicio
        self.tiempo_ensamblar = tiempo_ensamblar
        self.siguiente = None  # Apunta al siguiente nodo

class ListaEPendientes:
    def __init__(self):
        self.primero = None

    def insertar(self, linea, componente, tiempo_inicio, tiempo_ensamblar):
        nuevo_nodo = NodoEP(linea, componente, tiempo_inicio, tiempo_ensamblar)
        if not self.primero:
            self.primero = nuevo_nodo
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def imprimir(self):
        actual = self.primero
        while actual:
            print(f"Línea: {actual.linea}, Componente: {actual.componente}, Tiempo Inicio: {actual.tiempo_inicio}, Tiempo Ensamblar: {actual.tiempo_ensamblar}")
            actual = actual.siguiente
