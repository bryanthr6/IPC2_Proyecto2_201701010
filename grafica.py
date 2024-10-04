from graphviz import Digraph

def generar_grafico_elaboracion(producto, elaboracion):
    """
    Genera un gráfico usando Graphviz para visualizar la secuencia de elaboración de un producto.
    
    :param producto: Nombre del producto.
    :param elaboracion: Cadena que representa la secuencia de ensamblaje (e.g., 'L1C2 L4C1 L3C3 L5C0 L2C2').
    """
    # Crear un objeto Digraph de Graphviz
    dot = Digraph(comment=f'Proceso de ensamblaje para {producto}')
    
    # Separar la cadena de elaboración en una lista de acciones
    acciones = elaboracion.split()

    # Agregar nodos y flechas entre ellos
    for i in range(len(acciones) - 1):
        dot.node(acciones[i], acciones[i])  # Crear nodo para la acción actual
        dot.node(acciones[i+1], acciones[i+1])  # Crear nodo para la siguiente acción
        dot.edge(acciones[i], acciones[i+1])  # Crear una flecha de la acción actual a la siguiente
    
    # Guardar el archivo .gv (Graphviz)
    nombre_archivo = f"grafico_{producto.replace(' ', '_')}.gv"
    dot.render(nombre_archivo, view=False)  # Puedes usar view=True para abrir el gráfico automáticamente
    print(f"Gráfico generado: {nombre_archivo}")

    return nombre_archivo
