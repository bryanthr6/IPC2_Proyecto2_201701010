#calcular_tiempo.py
import re  # Usaremos expresiones regulares
from lista_posicion import Lista_Posicion  # Importar la nueva clase para las posiciones

def calcular_tiempo_ensamblaje(maquina):
    print("Seleccione un producto para calcular el tiempo de ensamblaje:")
    
    # Recorrer la lista enlazada de productos
    actual_producto = maquina.lista_productos.primero
    index = 1

    # Mostrar productos disponibles
    while actual_producto:
        print(f"{index}. {actual_producto.producto.nombre}")
        actual_producto = actual_producto.siguiente
        index += 1

    seleccion = int(input("Ingrese el número del producto: "))
    
    # Reiniciar el puntero a la cabeza de la lista enlazada
    actual_producto = maquina.lista_productos.primero
    contador = 1

    # Encontrar el producto seleccionado
    while actual_producto and contador < seleccion:
        actual_producto = actual_producto.siguiente
        contador += 1

    # Si no se encontró el producto, mostrar error
    if not actual_producto:
        print("ERROR: Producto no encontrado.")
        return

    # Obtener las instrucciones de ensamblaje
    producto = actual_producto.producto
    instrucciones = producto.elaboracion.split()  # Asumiendo que las instrucciones están separadas por espacios
    tiempo_total = 0
    posiciones = Lista_Posicion()  # Crear la lista enlazada para las posiciones de los brazos

    # Procesar cada instrucción
    for instruccion in instrucciones:
        # Usar expresión regular para extraer los números de línea y componente
        match = re.match(r'L(\d+)C(\d+)', instruccion)
        if not match:
            print(f"ERROR: Instrucción no válida '{instruccion}'")
            continue

        linea = int(match.group(1))  # Obtener el número de línea
        componente = int(match.group(2))  # Obtener el número de componente

        # Obtener la posición actual del brazo en esta línea
        posicion_anterior = posiciones.obtener_posicion(linea)

        # Calcular el tiempo para mover el brazo
        tiempo_mover_brazo = abs(componente - posicion_anterior)  # El brazo tarda en moverse la diferencia de componentes
        tiempo_ensamblar = maquina.tiempo_ensamblaje  # Tiempo de ensamblaje por componente

        # Actualizar la posición del brazo en esta línea
        posiciones.insertar_o_actualizar(linea, componente)

        print(f"Moviendo brazo a la línea {linea}, componente {componente}... (Tarda {tiempo_mover_brazo} segundos)")
        tiempo_total += tiempo_mover_brazo
        print(f"Ensamblando componente {componente}... (Tarda {tiempo_ensamblar} segundos)")
        tiempo_total += tiempo_ensamblar

    print(f"El tiempo total para ensamblar el producto '{producto.nombre}' es: {tiempo_total} segundos")
