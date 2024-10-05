from lista_posicion import Lista_Posicion  # Importar la nueva clase para las posiciones
import re  # Usaremos expresiones regulares
from grafico import generar_grafico  # Importar la función para generar la gráfica

def calcular_tiempo_ensamblaje(maquina):
    print("Seleccione un producto para calcular el tiempo de ensamblaje:")
    
    actual_producto = maquina.lista_productos.primero
    index = 1

    # Mostrar productos disponibles
    while actual_producto:
        print(f"{index}. {actual_producto.producto.nombre}")
        actual_producto = actual_producto.siguiente
        index += 1

    seleccion = int(input("Ingrese el número del producto: "))
    
    actual_producto = maquina.lista_productos.primero
    contador = 1

    # Encontrar el producto seleccionado
    while actual_producto and contador < seleccion:
        actual_producto = actual_producto.siguiente
        contador += 1

    if not actual_producto:
        print("ERROR: Producto no encontrado.")
        return

    # Obtener las instrucciones de ensamblaje
    producto = actual_producto.producto
    instrucciones = producto.elaboracion.split()
    tiempo_total = 0
    posiciones = Lista_Posicion()

    # Procesar las instrucciones
    for instruccion in instrucciones:
        match = re.match(r'L(\d+)C(\d+)', instruccion)
        if not match:
            print(f"ERROR: Instrucción no válida '{instruccion}'")
            continue

        linea = int(match.group(1))
        componente = int(match.group(2))

        posicion_anterior = posiciones.obtener_posicion(linea)

        tiempo_mover_brazo = abs(componente - posicion_anterior)
        tiempo_ensamblar = maquina.tiempo_ensamblaje

        posiciones.insertar_o_actualizar(linea, componente)

        print(f"Moviendo brazo a la línea {linea}, componente {componente}... (Tarda {tiempo_mover_brazo} segundos)")
        tiempo_total += tiempo_mover_brazo
        print(f"Ensamblando componente {componente}... (Tarda {tiempo_ensamblar} segundos)")
        tiempo_total += tiempo_ensamblar

    print(f"El tiempo total para ensamblar el producto '{producto.nombre}' es: {tiempo_total} segundos")

    # Preguntar al usuario si quiere generar la gráfica
    generar_grafica = input("¿Desea generar una gráfica de este ensamblaje? (s/n): ")
    
    if generar_grafica.lower() == 's':
        ruta_salida = input("Ingrese la ruta donde desea guardar la gráfica (sin extensión): ")
        generar_grafico(producto.nombre, maquina.nombre, producto.elaboracion, ruta_salida)

