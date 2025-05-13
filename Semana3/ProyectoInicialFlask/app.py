from flask import Flask, render_template
from modules import reportes

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route("/reportes")
def modulo_reportes():
    return reportes.mostrar_reporte()
0119
if __name__ == '__main__':
    app.run(debug=True)
