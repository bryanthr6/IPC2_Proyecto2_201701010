from flask import Flask, render_template, request, flash, redirect, url_for
import os
from cargar import cargar_archivo
from lista_maquinas import Lista_Maquinas

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
        archivo = request.files.get('archivo')
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

    # Buscar la máquina seleccionada en la lista enlazada
    actual = lista_maquinas.primero
    while actual:
        if actual.maquina.nombre == maquina_seleccionada:
            # Recorrer la lista de productos de la máquina seleccionada y generar las opciones HTML
            actual_producto = actual.maquina.lista_productos.primero
            while actual_producto:
                productos_html += f'<option value="{actual_producto.producto.nombre}">{actual_producto.producto.nombre}</option>'
                actual_producto = actual_producto.siguiente
            break
        actual = actual.siguiente

    data = {
        'title': 'IPC2_Proyecto2_201701010',
        'content': f'Productos disponibles para {maquina_seleccionada}'
    }

    # Volvemos a cargar las máquinas para seguir mostrando el combo box de máquinas
    maquinas_html = ""
    actual = lista_maquinas.primero
    while actual:
        maquinas_html += f'<option value="{actual.maquina.nombre}">{actual.maquina.nombre}</option>'
        actual = actual.siguiente

    return render_template('index.html', data=data, maquinas_html=maquinas_html, productos_html=productos_html)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
