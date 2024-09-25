# simulador.py
import xml.etree.ElementTree as ET
from lista_maquina import ListaEnlazadaMaquinas
from maquina import Maquina

class Simulador:
    def __init__(self):
        self.maquinas = ListaEnlazadaMaquinas()  # Lista enlazada de máquinas

    def cargar_maquina_desde_xml(self, archivo_xml):
        tree = ET.parse(archivo_xml)
        root = tree.getroot()

        for maquina in root.findall("Maquina"):
            nombre = maquina.find("NombreMaquina").text.strip()
            cantidad_lineas = int(maquina.find("CantidadLineasProduccion").text)
            cantidad_componentes = int(maquina.find("CantidadComponentes").text)
            tiempo_ensamblaje = int(maquina.find("TiempoEnsamblaje").text)
            
            nueva_maquina = Maquina(nombre, cantidad_lineas)
            
            # Agregar productos a la máquina
            for producto in maquina.find("ListadoProductos").findall("Producto"):
                nombre_producto = producto.find("nombre").text.strip()
                secuencia = producto.find("elaboracion").text.strip()
                # Guardamos el nombre del producto y la secuencia de ensamblaje
                nueva_maquina.agregar_producto(nombre_producto, secuencia)

            self.maquinas.agregar_maquina(nueva_maquina)

    def ejecutar_simulacion(self):
        # Aquí va la lógica para simular el ensamblaje de cada máquina
        pass

    # En simulador.py, en la función mostrar_reporte

    def mostrar_reporte(self):
        actual = self.maquinas.cabeza
        while actual is not None:
            maquina = actual.maquina
            for producto in maquina.productos:
                print(f"Producto: {producto.nombre}")
                print(f"{'Tiempo':<10} {'Línea 1':<10} {'Línea 2':<10} {'Línea 3':<10}")
                
                # Aquí simulamos el proceso de ensamblaje (ejemplo simple)
                tiempo = 1
                for paso in producto.secuencia_ensamblaje:
                    linea, componente = paso.split("C")
                    linea = linea.replace("L", "")
                    # Generar un reporte paso a paso (ejemplo básico)
                    print(f"{tiempo:<10} {'Ensamblar' if linea == '1' else '':<10} {'Ensamblar' if linea == '2' else '':<10} {'Ensamblar' if linea == '3' else '':<10}")
                    tiempo += 1
                print()  # Salto de línea entre productos
            actual = actual.siguiente

