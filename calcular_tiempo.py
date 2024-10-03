# calcular_tiempo.py
import re  # Usaremos expresiones regulares
from lista_posicion import Lista_Posicion  # Importar la clase para las posiciones
from lista_historial import Lista_Historial  # Importar la lista enlazada para el historial

def calcular_tiempo_ensamblaje(maquina, producto):
    instrucciones = producto.elaboracion.split()  # Asumiendo que las instrucciones están separadas por espacios
    tiempo_total = 0
    posiciones = Lista_Posicion()  # Crear la lista enlazada para las posiciones de los brazos
    historial = Lista_Historial()  # Usar la lista enlazada para almacenar los movimientos y ensamblajes
    segundos_accion = {}  # Guardar acciones por segundo y línea de producción (clave: segundo)

    for instruccion in instrucciones:
        match = re.match(r'L(\d+)C(\d+)', instruccion)
        if not match:
            historial.insertar(f"ERROR: Instrucción no válida '{instruccion}'")
            continue

        linea = int(match.group(1))  # Obtener el número de línea
        componente = int(match.group(2))  # Obtener el número de componente
        posicion_anterior = posiciones.obtener_posicion(linea)
        tiempo_mover_brazo = abs(componente - posicion_anterior)
        tiempo_ensamblar = maquina.tiempo_ensamblaje

        # Actualizar la posición del brazo
        posiciones.insertar_o_actualizar(linea, componente)

        # Almacenar el movimiento del brazo
        for segundo in range(tiempo_total + 1, tiempo_total + 1 + tiempo_mover_brazo):
            if segundo not in segundos_accion:
                segundos_accion[segundo] = {}
            segundos_accion[segundo][linea] = f"Mover brazo a componente {componente} (tarda {tiempo_mover_brazo} segundos)"
        tiempo_total += tiempo_mover_brazo

        # Almacenar el ensamblaje
        for segundo in range(tiempo_total + 1, tiempo_total + 1 + tiempo_ensamblar):
            if segundo not in segundos_accion:
                segundos_accion[segundo] = {}
            segundos_accion[segundo][linea] = f"Ensamblar componente {componente} (tarda {tiempo_ensamblar} segundos)"
        tiempo_total += tiempo_ensamblar

    # Retornar el historial de acciones por segundo
    return segundos_accion, tiempo_total
