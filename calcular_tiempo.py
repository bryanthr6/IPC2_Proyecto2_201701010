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

    # Procesar cada instrucción
    for instruccion in instrucciones:
        # Obtener la línea y componente de la instrucción (e.g., L1C2)
        linea = int(instruccion[1])  # Obtener el número de línea
        componente = int(instruccion[3])  # Obtener el número de componente

        # Calcular el tiempo para mover el brazo y ensamblar el componente
        tiempo_mover_brazo = componente  # Tarda `componente` segundos en moverse
        tiempo_ensamblar = maquina.tiempo_ensamblaje  # Tiempo de ensamblaje por componente

        print(f"Moviendo brazo a la línea {linea}, componente {componente}... (Tarda {tiempo_mover_brazo} segundos)")
        tiempo_total += tiempo_mover_brazo
        print(f"Ensamblando componente {componente}... (Tarda {tiempo_ensamblar} segundos)")
        tiempo_total += tiempo_ensamblar

    print(f"El tiempo total para ensamblar el producto '{producto.nombre}' es: {tiempo_total} segundos")
