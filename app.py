from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    data={
        'title':'IPC2_Proyecto2_201701010',
        'content':'Bienvenido a la pagina principal'
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)