from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse, FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import mysql.connector
import xlsxwriter
import os
from datetime import datetime

app = FastAPI()

# Configuraciones
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'flask_db'
}

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM producto")
    productos = cursor.fetchall()
    cursor.close()
    conn.close()
    return templates.TemplateResponse("index.html", {"request": request, "productos": productos})

@app.post("/agregar")
def agregar(nombre: str = Form(...), precio_unitario: float = Form(...), cantidad: int = Form(...)):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO producto (nombre, precio_unitario, cantidad) VALUES (%s, %s, %s)",
                   (nombre, precio_unitario, cantidad))
    conn.commit()
    cursor.close()
    conn.close()
    return RedirectResponse(url="/", status_code=303)

@app.get("/eliminar/{id}")
def eliminar(id: int):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM producto WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return RedirectResponse(url="/", status_code=303)

@app.get("/generar_informe")
def generar_informe():
    conn = mysql.connector.connect(**db_config)
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM producto")
    productos = cur.fetchall()

    downloads_dir = os.path.join(os.getcwd(), 'downloads')
    os.makedirs(downloads_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    excel_file = os.path.join(downloads_dir, f'informe_inventario_{timestamp}.xlsx')

    workbook = xlsxwriter.Workbook(excel_file)
    worksheet = workbook.add_worksheet('Inventario')
    titulo_formato = workbook.add_format({'bold': True, 'font_size': 14, 'align': 'center', 'valign': 'vcenter'})
    cabecera_formato = workbook.add_format({'bold': True, 'bg_color': '#CCCCCC', 'border': 1})

    worksheet.merge_range('A1:E1', 'INFORME DE INVENTARIO', titulo_formato)
    worksheet.set_column('A:A', 10)
    worksheet.set_column('B:B', 30)
    worksheet.set_column('C:C', 15)
    worksheet.set_column('D:D', 15)
    worksheet.set_column('E:E', 20)

    worksheet.write('A3', 'ID', cabecera_formato)
    worksheet.write('B3', 'Nombre', cabecera_formato)
    worksheet.write('C3', 'Precio Unitario', cabecera_formato)
    worksheet.write('D3', 'Cantidad', cabecera_formato)
    worksheet.write('E3', 'Valor Total', cabecera_formato)

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

    workbook.close()
    cur.close()
    conn.close()

    return FileResponse(path=excel_file, filename=os.path.basename(excel_file), media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
