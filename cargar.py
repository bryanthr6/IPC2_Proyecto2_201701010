# cargar.py
import xml.etree.ElementTree as ET
import re
from lista_maquinas import Lista_Maquinas
from lista_productos import Lista_Productos
from maquina import Maquina
from producto import Producto

def cargar_archivo(ruta):
    try:
        tree = ET.parse(ruta)
        root = tree.getroot()
        
        lista_maquinas = Lista_Maquinas()
        
        # Iterar sobre las máquinas en el archivo XML
        for maquina_xml in root.findall('Maquina'):
            nombre = maquina_xml.find('NombreMaquina').text.strip()
            lineas = int(maquina_xml.find('CantidadLineasProduccion').text.strip())
            componentes = int(maquina_xml.find('CantidadComponentes').text.strip())
            tiempo_ensamblaje = int(maquina_xml.find('TiempoEnsamblaje').text.strip())
            
            # Crear una lista enlazada de productos
            lista_productos = Lista_Productos()
            
            # Procesar cada producto
            for producto_xml in maquina_xml.find('ListadoProductos').findall('Producto'):
                nombre_producto = producto_xml.find('nombre').text.strip()
                
                # Limpiar la cadena de elaboración, eliminando espacios extras
                elaboracion = producto_xml.find('elaboracion').text.strip()
                elaboracion_limpia = re.sub(r'\s+', ' ', elaboracion)  # Reemplazar múltiples espacios por uno solo
                
                producto = Producto(nombre_producto, elaboracion_limpia)
                lista_productos.insertar(producto)  # Insertar el producto en la lista enlazada
            
            # Crear objeto Maquina con la lista enlazada de productos
            maquina = Maquina(nombre, lineas, componentes, tiempo_ensamblaje, lista_productos)
            lista_maquinas.insertar(maquina)
        
        print("Archivo cargado y máquinas procesadas exitosamente.")
        return lista_maquinas
    
    except FileNotFoundError:
        print(f"ERROR: El archivo '{ruta}' no se encontró.")
    except ET.ParseError:
        print("ERROR: No se pudo parsear el archivo XML.")
    except Exception as e:
        print(f"ERROR: {e}")
