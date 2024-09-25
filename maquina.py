from lista_ensamblaje import ListaLineasEnsamblaje

# maquina.py
class Maquina:
    def __init__(self, nombre, cantidad_lineas):
        self.nombre = nombre
        self.lineas = ListaLineasEnsamblaje()  # Lista enlazada de líneas de ensamblaje
        self.productos = []  # Lista de productos de esta máquina (no nativa)
        for i in range(cantidad_lineas):
            self.lineas.agregar_linea(i + 1)  # Agregar líneas a la máquina

    def agregar_producto(self, nombre_producto, secuencia):
        # Crear un diccionario o estructura que guarde el nombre del producto y la secuencia
        self.productos.append(Producto(nombre_producto, secuencia))

    def mover_brazo(self, numero_linea, numero_componente):
        # Mueve el brazo en la línea indicada al componente especificado
        pass

    def ensamblar_componente(self, numero_linea):
        # Ensambla el componente en la línea de ensamblaje indicada
        pass

class Producto:
    def __init__(self, nombre, secuencia_ensamblaje):
        self.nombre = nombre
        self.secuencia_ensamblaje = secuencia_ensamblaje.split()  # Separar por espacios
