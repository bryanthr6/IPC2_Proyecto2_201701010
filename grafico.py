import graphviz

def generar_grafico(producto, maquina, instrucciones, ruta_salida):
    # Crear un nuevo gráfico de tipo digraph (direccional)
    dot = graphviz.Digraph(comment=f'Máquina: {maquina}, Producto: {producto}')

    # Configuración del gráfico para que sea horizontal y con nodos en cuadros
    dot.attr(rankdir='LR')  # Dirección de izquierda a derecha (horizontal)
    dot.attr('node', shape='box')  # Forma de los nodos como cuadros

    # Agregar la etiqueta del gráfico con el nombre del producto y la máquina
    dot.attr(label=f'Nombre de la máquina: {maquina}\nNombre del producto: {producto}\n')
    
    # Procesar las instrucciones para generar las conexiones
    nodos = instrucciones.split()  # Separar las instrucciones por espacio
    for i in range(len(nodos) - 1):
        dot.edge(nodos[i], nodos[i + 1])  # Conectar los nodos sin etiqueta en la flecha

    # Guardar el gráfico en el archivo especificado
    dot.render(ruta_salida, format='png', cleanup=True)
    print(f"Gráfica generada y guardada en: {ruta_salida}.png")
