import xml.etree.ElementTree as ET

def generar_salida_xml(maquina, producto, segundos_accion, tiempo_total, archivo_salida):
    # Crear el elemento raíz
    salida_simulacion = ET.Element('SalidaSimulacion')

    # Crear el nodo de la máquina
    maquina_element = ET.SubElement(salida_simulacion, 'Maquina')
    nombre_maquina = ET.SubElement(maquina_element, 'Nombre')
    nombre_maquina.text = maquina.nombre

    # Crear el listado de productos
    listado_productos = ET.SubElement(maquina_element, 'ListadoProductos')
    producto_element = ET.SubElement(listado_productos, 'Producto')
    
    # Nombre del producto
    nombre_producto = ET.SubElement(producto_element, 'Nombre')
    nombre_producto.text = producto.nombre

    # Tiempo total
    tiempo_total_element = ET.SubElement(producto_element, 'TiempoTotal')
    tiempo_total_element.text = str(tiempo_total)

    # Elaboración óptima
    elaboracion_optima = ET.SubElement(producto_element, 'ElaboracionOptima')

    for segundo, acciones in segundos_accion.items():
        tiempo_element = ET.SubElement(elaboracion_optima, 'Tiempo', NoSegundo=str(segundo))

        for linea, accion in acciones.items():
            linea_element = ET.SubElement(tiempo_element, 'LineaEnsamblaje', NoLinea=str(linea))
            linea_element.text = accion

    # Escribir el archivo XML
    tree = ET.ElementTree(salida_simulacion)
    tree.write(archivo_salida, encoding="utf-8", xml_declaration=True)
