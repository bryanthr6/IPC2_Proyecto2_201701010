# calcular_tiempo.py
import re
from lista_posicion import Lista_Posicion
from lista_historial import Lista_Historial
from segundos_accion import Lista_SegundosAccion

def calcular_tiempo_ensamblaje(maquina, producto):
    instrucciones = producto.elaboracion.split()
    tiempo_total = 0
    posiciones = Lista_Posicion()
    historial = Lista_Historial()
    segundos_accion = Lista_SegundosAccion()

    for instruccion in instrucciones:
        match = re.match(r'L(\d+)C(\d+)', instruccion)
        if not match:
            historial.insertar(f"ERROR: Instrucción no válida '{instruccion}'")
            continue

        linea = int(match.group(1))
        componente = int(match.group(2))
        posicion_anterior = posiciones.obtener_posicion(linea)
        tiempo_mover_brazo = abs(componente - posicion_anterior)
        tiempo_ensamblar = maquina.tiempo_ensamblaje

        posiciones.insertar_o_actualizar(linea, componente)

        for segundo in range(tiempo_total + 1, tiempo_total + 1 + tiempo_mover_brazo):
            segundos_accion.insertar(segundo, linea, f"Mover brazo a componente {componente} (tarda {tiempo_mover_brazo} segundos)")
        tiempo_total += tiempo_mover_brazo

        for segundo in range(tiempo_total + 1, tiempo_total + 1 + tiempo_ensamblar):
            segundos_accion.insertar(segundo, linea, f"Ensamblar componente {componente} (tarda {tiempo_ensamblar} segundos)")
        tiempo_total += tiempo_ensamblar

    return segundos_accion.obtener_acciones(), tiempo_total
