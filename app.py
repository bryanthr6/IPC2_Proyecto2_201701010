from flask import Flask, render_template, request, flash, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necesario para mostrar mensajes flash

# Crear la carpeta 'uploads' si no existe
if not os.path.exists('./uploads'):
    os.makedirs('./uploads')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Si el usuario sube un archivo XML
        if 'archivo' not in request.files:
            flash('No se seleccionó ningún archivo')
            return redirect(request.url)
        
        archivo = request.files['archivo']
        
        if archivo.filename == '':
            flash('No se seleccionó ningún archivo')
            return redirect(request.url)
        
        if archivo:
            # Guardar el archivo en la carpeta uploads
            ruta = os.path.join('./uploads', archivo.filename)
            archivo.save(ruta)
            flash('Archivo cargado exitosamente')
            return redirect(url_for('index'))

    data = {
        'title': 'IPC2_Proyecto2_201701010',
        'content': 'Bienvenido a la página principal'
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
