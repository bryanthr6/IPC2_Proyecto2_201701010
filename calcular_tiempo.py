import re
from lista_posicion import Lista_Posicion
from lista_tabla import Lista_Tabla

def calcular_tiempo_ensamblaje(maquina, producto):
    instrucciones = producto.elaboracion.split()  # Asumiendo que las instrucciones están separadas por espacios
    tiempo_total = 0
    posiciones = Lista_Posicion()  # Crear la lista enlazada para las posiciones de los brazos
    tabla = Lista_Tabla()  # Lista enlazada para almacenar la tabla de ensamblaje

    # Procesar cada instrucción
    tiempo = 1
    for instruccion in instrucciones:
        match = re.match(r'L(\d+)C(\d+)', instruccion)
        if not match:
            continue

        linea = int(match.group(1))  # Obtener el número de línea
        componente = int(match.group(2))  # Obtener el número de componente

        # Obtener la posición actual del brazo en esta línea
        posicion_anterior = posiciones.obtener_posicion(linea)

        # Calcular el tiempo para mover el brazo
        tiempo_mover_brazo = abs(componente - posicion_anterior)  # Tiempo en moverse
        tiempo_ensamblar = maquina.tiempo_ensamblaje  # Tiempo de ensamblaje

        # Registrar el movimiento del brazo en cada segundo
        for _ in range(tiempo_mover_brazo):
            lineas_acciones = [""] * maquina.lineas  # Creamos una lista para representar las acciones en cada línea
            lineas_acciones[linea - 1] = f'Mover a componente {componente}'
            tabla.insertar(tiempo, lineas_acciones)
            tiempo += 1

        # Registrar el ensamblaje
        lineas_acciones = [""] * maquina.lineas
        lineas_acciones[linea - 1] = f'Ensamblar componente {componente}'
        tabla.insertar(tiempo, lineas_acciones)
        tiempo += tiempo_ensamblar

        # Actualizar la posición del brazo en esta línea
        posiciones.insertar_o_actualizar(linea, componente)

    resultado = f"El tiempo total para ensamblar el producto '{producto.nombre}' es: {tiempo} segundos"
    return resultado, tabla
