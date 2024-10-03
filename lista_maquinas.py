#lista_maquinas.py
from nodo_maquina import Nodo_Maquina
from maquina import Maquina

class Lista_Maquinas:
    def __init__(self):
        self.primero = None

    def insertar(self, maquina):
        if not self.primero:
            self.primero = Nodo_Maquina(maquina)

        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = Nodo_Maquina(maquina)

    def imprimir(self):
        actual = self.primero
        while actual:
            print(f"Nombre: {actual.maquina.nombre}")
            print(f"Lineas: {actual.maquina.lineas}")
            print(f"Componentes: {actual.maquina.componentes}")
            print(f"Tiempo de ensamblaje: {actual.maquina.tiempo_ensamblaje}")
            actual.maquina.lista_productos.imprimir()
            print('\n')
            actual = actual.siguiente