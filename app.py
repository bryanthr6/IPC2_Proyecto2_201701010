from flask import Flask, render_template, request, flash, redirect, url_for
import os
from cargar import cargar_archivo
from calcular_tiempo import calcular_tiempo_ensamblaje
from grafica import generar_grafico_elaboracion  # Importa la función de generar gráfico
from lista_maquinas import Lista_Maquinas
import xml.etree.ElementTree as ET


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

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Crear la carpeta 'uploads' si no existe
if not os.path.exists('./uploads'):
    os.makedirs('./uploads')

# Almacenar la lista de máquinas globalmente para la sesión
lista_maquinas = Lista_Maquinas()

@app.route('/', methods=['GET', 'POST'])
def index():
    data = {
        'title': 'IPC2_Proyecto2_201701010',
        'content': 'Bienvenido a la página principal'
    }

    maquinas_html = ""  # String para almacenar las opciones de máquinas
    productos_html = ""  # String para almacenar los productos de una máquina seleccionada

    if request.method == 'POST':
        archivo = request.files.get('archivo')  # Obtenemos el archivo subido
        if archivo and archivo.filename.endswith('.xml'):
            try:
                ruta_archivo = os.path.join('./uploads', archivo.filename)
                archivo.save(ruta_archivo)

                # Procesar el archivo XML y cargar los datos en lista_maquinas
                cargar_archivo(ruta_archivo, lista_maquinas)

                # Recorrer la lista enlazada de máquinas y generar las opciones HTML
                actual = lista_maquinas.primero
                while actual:
                    maquinas_html += f'<option value="{actual.maquina.nombre}">{actual.maquina.nombre}</option>'
                    actual = actual.siguiente

                flash('Archivo cargado exitosamente', 'success')

            except Exception as e:
                flash(f'Error al procesar el archivo: {str(e)}', 'danger')
        else:
            flash('Error: Solo se permiten archivos XML', 'danger')

    return render_template('index.html', data=data, maquinas_html=maquinas_html, productos_html=productos_html)

@app.route('/seleccionar-maquina', methods=['POST'])
def seleccionar_maquina():
    maquina_seleccionada = request.form.get('maquina')
    productos_html = ""
    tiempo_ensamblaje = None
    componentes = None
    lineas = None

    # Buscar la máquina seleccionada en la lista enlazada
    actual = lista_maquinas.primero
    while actual:
        if actual.maquina.nombre == maquina_seleccionada:
            # Obtener información adicional de la máquina
            tiempo_ensamblaje = actual.maquina.tiempo_ensamblaje
            componentes = actual.maquina.componentes
            lineas = actual.maquina.lineas
            
            # Recorrer la lista de productos de la máquina seleccionada y generar las opciones HTML
            actual_producto = actual.maquina.lista_productos.primero
            while actual_producto:
                productos_html += f'<option value="{actual_producto.producto.nombre}">{actual_producto.producto.nombre}</option>'
                actual_producto = actual_producto.siguiente
            break
        actual = actual.siguiente

    data = {
        'title': 'IPC2_Proyecto2_201701010',
        'content': f'Productos disponibles para {maquina_seleccionada}',
    }

    # Volvemos a cargar las máquinas para seguir mostrando el combo box de máquinas
    maquinas_html = ""
    actual = lista_maquinas.primero
    while actual:
        maquinas_html += f'<option value="{actual.maquina.nombre}">{actual.maquina.nombre}</option>'
        actual = actual.siguiente

    # Asegúrate de pasar maquina_seleccionada al template
    return render_template('index.html', data=data, maquinas_html=maquinas_html, productos_html=productos_html, 
                           tiempo_ensamblaje=tiempo_ensamblaje, componentes=componentes, lineas=lineas, 
                           maquina_seleccionada=maquina_seleccionada)

@app.route('/seleccionar-producto', methods=['POST'])
def seleccionar_producto():
    producto_seleccionado = request.form.get('producto')
    maquina_seleccionada = request.form.get('maquina')

    # Buscar la máquina seleccionada en la lista enlazada
    actual = lista_maquinas.primero
    maquina = None
    while actual:
        if actual.maquina.nombre == maquina_seleccionada:
            maquina = actual.maquina
            break
        actual = actual.siguiente

    if maquina is None:
        flash(f"Error: La máquina '{maquina_seleccionada}' no fue encontrada.", "danger")
        return redirect(url_for('index'))

    # Buscar el producto seleccionado en la lista de productos de la máquina
    actual_producto = maquina.lista_productos.primero
    producto = None
    while actual_producto:
        if actual_producto.producto.nombre == producto_seleccionado:
            producto = actual_producto.producto
            break
        actual_producto = actual_producto.siguiente

    if producto is None:
        flash(f"Error: El producto '{producto_seleccionado}' no fue encontrado en la máquina '{maquina_seleccionada}'.", "danger")
        return redirect(url_for('index'))

    # Calcular el historial de ensamblaje
    segundos_accion, tiempo_total = calcular_tiempo_ensamblaje(maquina, producto)

    # Renderizar la plantilla de resultados con el historial y las acciones por segundo
    return render_template('resultados.html', producto=producto.nombre, segundos_accion=segundos_accion, tiempo_total=tiempo_total, lineas=maquina.lineas)


@app.route('/resultados')
def resultados():
    producto = request.args.get('producto')
    lineas = request.args.get('lineas')

    data = {
        'title': 'Resultados de Selección',
        'producto': producto,
        'lineas': lineas
    }
    return render_template('resultados.html', data=data)

@app.route('/generar-resumen', methods=['POST'])
def generar_resumen():
    nombre_archivo = request.form['nombre_archivo']
    ubicacion_archivo = request.form['ubicacion_archivo']
    producto = request.form['producto']
    segundos_accion = eval(request.form['segundos_accion'])
    lineas = int(request.form['lineas'])
    tiempo_total = int(request.form['tiempo_total'])

    try:
        root = ET.Element('ResumenEnsamblaje')
        ET.SubElement(root, 'Producto').text = producto
        ET.SubElement(root, 'TiempoTotal').text = str(tiempo_total)
        historial_element = ET.SubElement(root, 'Historial')

        for segundo in range(1, tiempo_total + 1):
            segundo_element = ET.SubElement(historial_element, 'Segundo', numero=str(segundo))
            for linea in range(1, lineas + 1):
                if segundo in segundos_accion and linea in segundos_accion[segundo]:
                    accion = segundos_accion[segundo][linea]
                else:
                    accion = "No hacer nada"
                ET.SubElement(segundo_element, 'Linea', numero=str(linea)).text = accion

        indent(root)  # Formatea el árbol XML
        tree = ET.ElementTree(root)
        ruta_completa = os.path.join(ubicacion_archivo, nombre_archivo)
        tree.write(ruta_completa, encoding='utf-8', xml_declaration=True)

        flash(f'Resumen XML generado y guardado en {ruta_completa}', 'success')
    except Exception as e:
        flash(f'Error al generar el resumen XML: {str(e)}', 'danger')

    return redirect(url_for('resultados', producto=producto, lineas=lineas))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
