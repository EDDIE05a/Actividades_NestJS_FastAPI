import mysql.connector
from flask import Flask, send_file, render_template, request, redirect, url_for
import xlsxwriter
import os
from datetime import datetime


app = Flask(__name__)

# Configuración básica de la base de datos
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'flask_db'
}

@app.route('/')
def index():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM producto")
    productos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', productos=productos)

@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    precio = request.form['precio_unitario']
    cantidad = request.form['cantidad']

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO producto (nombre, precio_unitario, cantidad) VALUES (%s, %s, %s)",
                   (nombre, precio, cantidad))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/generar_informe')
def generar_informe():

    # Conectar a la base de datos usando db_config
    conn = mysql.connector.connect(**db_config)
    cur = conn.cursor(dictionary=True)  # Para obtener columnas con nombre

    # Obtener todos los productos
    cur.execute("SELECT * FROM producto")
    productos = cur.fetchall()

    # Crear carpeta downloads si no existe
    downloads_dir = os.path.join(os.getcwd(), 'downloads')
    os.makedirs(downloads_dir, exist_ok=True)

    # Nombre del archivo Excel
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    excel_file = os.path.join(downloads_dir, f'informe_inventario_{timestamp}.xlsx')

    # Crear archivo Excel
    workbook = xlsxwriter.Workbook(excel_file)
    worksheet = workbook.add_worksheet('Inventario')

    # Formatos
    titulo_formato = workbook.add_format({'bold': True, 'font_size': 14, 'align': 'center', 'valign': 'vcenter'})
    cabecera_formato = workbook.add_format({'bold': True, 'bg_color': '#CCCCCC', 'border': 1})

    worksheet.merge_range('A1:E1', 'INFORME DE INVENTARIO', titulo_formato)
    worksheet.set_column('A:A', 10)
    worksheet.set_column('B:B', 30)
    worksheet.set_column('C:C', 15)
    worksheet.set_column('D:D', 15)
    worksheet.set_column('E:E', 20)

    # Cabeceras
    worksheet.write('A3', 'ID', cabecera_formato)
    worksheet.write('B3', 'Nombre', cabecera_formato)
    worksheet.write('C3', 'Precio Unitario', cabecera_formato)
    worksheet.write('D3', 'Cantidad', cabecera_formato)
    worksheet.write('E3', 'Valor Total', cabecera_formato)

    # Datos
    fila = 3
    valor_inventario_total = 0

    for producto in productos:
        valor_total = float(producto['precio_unitario']) * int(producto['cantidad'])
        valor_inventario_total += valor_total

        worksheet.write(fila, 0, producto['id'])
        worksheet.write(fila, 1, producto['nombre'])
        worksheet.write(fila, 2, float(producto['precio_unitario']))
        worksheet.write(fila, 3, int(producto['cantidad']))
        worksheet.write(fila, 4, valor_total)
        fila += 1

    worksheet.write(fila + 1, 3, 'VALOR TOTAL DEL INVENTARIO:', cabecera_formato)
    worksheet.write(fila + 1, 4, valor_inventario_total)

    # Cerrar conexiones
    workbook.close()
    cur.close()
    conn.close()

    # Enviar archivo
    return send_file(excel_file, as_attachment=True)


@app.route('/eliminar/<int:id>')
def eliminar(id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM producto WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)
