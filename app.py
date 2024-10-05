from flask import Flask, render_template, request, redirect, url_for, flash
from cargar import cargar_archivo, lista_maquinas_acumuladas
from lista_posicion import Lista_Posicion
from grafico import generar_grafico
from lista_acciones import ListaAcciones
import xml.etree.ElementTree as ET  # Importa el módulo para trabajar con XML
import graphviz
import re
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necesario para usar mensajes flash

# Ruta principal que muestra el formulario y las máquinas cargadas
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'archivo' not in request.files:
            flash('No se ha seleccionado un archivo')
            return redirect(request.url)

        archivo = request.files['archivo']

        if archivo.filename == '':
            flash('No se ha seleccionado ningún archivo')
            return redirect(request.url)

        if archivo and archivo.filename.endswith('.xml'):
            ruta_archivo = os.path.join('./uploads', archivo.filename)  # Guardar el archivo en la carpeta 'uploads'
            archivo.save(ruta_archivo)
            cargar_archivo(ruta_archivo)  # Procesar el archivo XML
            flash('Archivo XML cargado y procesado correctamente')
        else:
            flash('El archivo debe ser XML')

    # Obtener la lista de máquinas procesadas
    maquinas_html = generar_maquinas_html()

    return render_template('index.html', data={'title': 'Carga de Máquinas', 'content': 'Sistema de Ensamblaje'}, maquinas_html=maquinas_html)

# Ruta que maneja la selección de la máquina
@app.route('/seleccionar-maquina', methods=['POST'])
def seleccionar_maquina():
    maquina_seleccionada = request.form['maquina']
    
    if not maquina_seleccionada:
        flash('No se ha seleccionado ninguna máquina')
        return redirect(url_for('index'))
    
    # Buscar la máquina seleccionada en la lista enlazada
    actual = lista_maquinas_acumuladas.primero
    maquina = None
    while actual:
        if actual.maquina.nombre == maquina_seleccionada:
            maquina = actual.maquina
            break
        actual = actual.siguiente

    if not maquina:
        flash('No se encontró la máquina seleccionada')
        return redirect(url_for('index'))

    # Obtener la información de la máquina seleccionada
    tiempo_ensamblaje = maquina.tiempo_ensamblaje
    componentes = maquina.componentes
    lineas = maquina.lineas

    # Obtener el HTML de los productos de la máquina
    productos_html = generar_productos_html(maquina.lista_productos)

    return render_template('index.html', 
                           data={'title': 'Máquina Seleccionada', 'content': 'Información de Ensamblaje'},
                           maquinas_html=generar_maquinas_html(),
                           maquina_seleccionada=maquina_seleccionada,
                           tiempo_ensamblaje=tiempo_ensamblaje,
                           componentes=componentes,
                           lineas=lineas,
                           productos_html=productos_html)


@app.route('/seleccionar-producto', methods=['POST'])
def seleccionar_producto():
    producto_seleccionado = request.form['producto']
    maquina_seleccionada = request.form['maquina']

    # Buscar la máquina seleccionada en la lista
    actual = lista_maquinas_acumuladas.primero
    maquina = None
    while actual:
        if actual.maquina.nombre == maquina_seleccionada:
            maquina = actual.maquina
            break
        actual = actual.siguiente

    if not maquina:
        flash('No se encontró la máquina seleccionada')
        return redirect(url_for('index'))

    # Buscar el producto seleccionado dentro de la máquina
    actual_producto = maquina.lista_productos.primero
    producto = None
    while actual_producto:
        if actual_producto.producto.nombre == producto_seleccionado:
            producto = actual_producto.producto
            break
        actual_producto = actual_producto.siguiente

    if not producto:
        flash('No se encontró el producto seleccionado')
        return redirect(url_for('index'))

    # Calcular el tiempo de ensamblaje
    segundos_accion, tiempo_total = calcular_ensamblaje(producto, maquina)

    return render_template('resultados.html',
                           producto=producto.nombre,
                           lineas=maquina.lineas,
                           tiempo_total=tiempo_total,
                           segundos_accion=segundos_accion,
                           elaboracion=producto.elaboracion)  # Se pasa la elaboración para mostrarla en la página
                           

# Lógica para calcular el ensamblaje y devolver la acción de cada segundo
def calcular_ensamblaje(producto, maquina):
    instrucciones = producto.elaboracion.split()
    lista_acciones = ListaAcciones()  # Reemplazo del diccionario por la lista enlazada
    posiciones = Lista_Posicion()  # Para registrar las posiciones de los componentes
    tiempo_total = 0

    for instruccion in instrucciones:
        match = re.match(r'L(\d+)C(\d+)', instruccion)
        if not match:
            print(f"ERROR: Instrucción no válida '{instruccion}'")
            continue

        linea = int(match.group(1))
        componente = int(match.group(2))

        # Salta si el componente es 0, ya que no debería ensamblarse
        if componente == 0:
            print(f"Ignorando componente {componente} en la línea {linea}, ya que no es válido")
            continue

        posicion_anterior = posiciones.obtener_posicion(linea)

        tiempo_mover_brazo = abs(componente - posicion_anterior)
        tiempo_ensamblar = maquina.tiempo_ensamblaje

        # Actualizar la posición del brazo en la línea actual
        posiciones.insertar_o_actualizar(linea, componente)

        # Guardar la acción para cada segundo de movimiento del brazo
        for segundo in range(tiempo_total + 1, tiempo_total + tiempo_mover_brazo + 1):
            lista_acciones.agregar_accion(segundo, linea, f"Moviendo brazo a componente {componente}")
            print(f"Guardando acción: Moviendo brazo a componente {componente} en el segundo {segundo} para la línea {linea}")
        tiempo_total += tiempo_mover_brazo

        # Guardar la acción para cada segundo de ensamblaje
        for segundo in range(tiempo_total + 1, tiempo_total + tiempo_ensamblar + 1):
            lista_acciones.agregar_accion(segundo, linea, f"Ensamblando componente {componente}")
            print(f"Guardando acción: Ensamblando componente {componente} en el segundo {segundo} para la línea {linea}")

        tiempo_total += tiempo_ensamblar

    return lista_acciones, tiempo_total




# Función para generar el HTML de las máquinas disponibles
def generar_maquinas_html():
    html = ""
    actual = lista_maquinas_acumuladas.primero
    while actual:
        html += f'<option value="{actual.maquina.nombre}">{actual.maquina.nombre}</option>'
        actual = actual.siguiente
    return html

# Función para generar el HTML de los productos disponibles de una máquina
def generar_productos_html(lista_productos):
    html = ""
    actual = lista_productos.primero
    while actual:
        html += f'<option value="{actual.producto.nombre}">{actual.producto.nombre}</option>'
        actual = actual.siguiente
    return html


def generar_grafico(producto, maquina, elaboracion, ruta_salida):
    # Creamos un nuevo objeto Digraph de Graphviz
    dot = graphviz.Digraph(comment=f'Proceso de Ensamblaje - {producto}', format='png')

    # Establecemos las opciones para que sea horizontal y los nodos sean cuadrados
    dot.attr(rankdir='LR')  # Dirección de izquierda a derecha
    dot.attr('node', shape='box')  # Los nodos tendrán forma de cuadro

    # Convertimos la secuencia de elaboracion en una lista
    secuencia = elaboracion.split()

    # Iteramos sobre los elementos de la secuencia para crear el gráfico
    for i in range(len(secuencia) - 1):
        dot.edge(secuencia[i], secuencia[i+1])

    # Guardamos el gráfico en la ruta de salida proporcionada
    dot.render(ruta_salida, format='png')
    print(f'Gráfico generado en {ruta_salida}.png')


@app.route('/generar-grafico', methods=['POST'])
def generar_grafico_route():
    nombre_archivo = request.form['nombre_archivo']
    ubicacion_archivo = request.form['ubicacion_archivo']
    producto = request.form['producto']
    elaboracion = request.form['elaboracion']  # Las instrucciones como 'L4C3 L2C0 L1C6...'
    maquina = request.form['maquina']  # El nombre de la máquina, si lo necesitas

    # Ruta de salida completa para el gráfico
    ruta_salida = os.path.join(ubicacion_archivo, nombre_archivo)

    try:
        generar_grafico(producto, maquina, elaboracion, ruta_salida)
        flash('Gráfico generado correctamente en: ' + ruta_salida + '.png')
    except Exception as e:
        flash('Error al generar el gráfico: ' + str(e))

    return redirect(url_for('index'))  # Redirige a la página de inicio o a la página anterior


def indent(elem, level=0):
    """Indenta un árbol XML para que sea más legible."""
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        for subelem in elem:
            indent(subelem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def generar_xml_salida(producto, tiempo_total, nombre_archivo, ubicacion):
    # Crear el elemento raíz del XML
    root = ET.Element("SalidaSimulacion")

    # Crear el elemento del producto
    producto_element = ET.SubElement(root, "Producto")
    ET.SubElement(producto_element, "Nombre").text = producto
    ET.SubElement(producto_element, "TiempoTotal").text = str(tiempo_total)

    # Indentar el árbol XML
    indent(root)

    # Escribir el XML en el archivo
    archivo_salida = os.path.join(ubicacion, nombre_archivo)
    tree = ET.ElementTree(root)
    tree.write(archivo_salida, encoding='utf-8', xml_declaration=True)

    print(f"Archivo XML generado: {archivo_salida}")



@app.route('/generar-resumen', methods=['POST'])
def generar_resumen():
    nombre_archivo = request.form['nombre_archivo']
    ubicacion_archivo = request.form['ubicacion_archivo']
    producto = request.form['producto']
    tiempo_total = int(request.form['tiempo_total'])

    # Generar el archivo XML con el producto y tiempo total
    try:
        generar_xml_salida(producto, tiempo_total, nombre_archivo, ubicacion_archivo)
        flash('Archivo XML generado correctamente.')
    except Exception as e:
        flash(f'Error al generar el archivo XML: {str(e)}')

    return redirect(url_for('index'))









if __name__ == '__main__':
    app.run(debug=True)
