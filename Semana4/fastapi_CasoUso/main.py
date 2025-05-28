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

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    
    # Obtener productos con sus categorías
    cursor.execute("""
        SELECT p.id, p.nombre, p.precio_unitario, p.cantidad, 
               c.nombre as categoria_nombre
        FROM producto p
        LEFT JOIN categoria c ON p.categoria_id = c.id
        ORDER BY p.id
    """)
    productos = cursor.fetchall()
    
    # Obtener categorías para el formulario
    cursor.execute("SELECT id, nombre FROM categoria ORDER BY nombre")
    categorias = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "productos": productos,
        "categorias": categorias
    })

@app.post("/agregar")
def agregar(nombre: str = Form(...), precio_unitario: float = Form(...), 
           cantidad: int = Form(...), categoria_id: int = Form(...)):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO producto (nombre, precio_unitario, cantidad, categoria_id) 
        VALUES (%s, %s, %s, %s)
    """, (nombre, precio_unitario, cantidad, categoria_id))
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

@app.post("/agregar_categoria")
def agregar_categoria(categoria_nombre: str = Form(...)):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO categoria (nombre) VALUES (%s)", (categoria_nombre,))
        conn.commit()
    except mysql.connector.IntegrityError:
        pass  # Categoría ya existe
    cursor.close()
    conn.close()
    return RedirectResponse(url="/", status_code=303)

@app.get("/generar_informe")
def generar_informe():
    conn = mysql.connector.connect(**db_config)
    cur = conn.cursor(dictionary=True)
    
    # Obtener productos con categorías
    cur.execute("""
        SELECT p.id, p.nombre, p.precio_unitario, p.cantidad,
               c.nombre as categoria_nombre
        FROM producto p
        LEFT JOIN categoria c ON p.categoria_id = c.id
        ORDER BY p.id
    """)
    productos = cur.fetchall()

    downloads_dir = os.path.join(os.getcwd(), 'downloads')
    os.makedirs(downloads_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    excel_file = os.path.join(downloads_dir, f'informe_inventario_{timestamp}.xlsx')

    workbook = xlsxwriter.Workbook(excel_file)
    worksheet = workbook.add_worksheet('Inventario')
    
    # Formatos
    titulo_formato = workbook.add_format({'bold': True, 'font_size': 14})
    cabecera_formato = workbook.add_format({'bold': True, 'bg_color': '#CCCCCC'})

    # Título y cabeceras
    worksheet.write('A1', 'INFORME DE INVENTARIO', titulo_formato)
    worksheet.write('A3', 'ID', cabecera_formato)
    worksheet.write('B3', 'Nombre', cabecera_formato)
    worksheet.write('C3', 'Precio Unitario', cabecera_formato)
    worksheet.write('D3', 'Cantidad', cabecera_formato)
    worksheet.write('E3', 'Categoría', cabecera_formato)
    worksheet.write('F3', 'Valor Total', cabecera_formato)

    # Datos
    fila = 3
    total_inventario = 0
    for producto in productos:
        valor_total = float(producto['precio_unitario']) * int(producto['cantidad'])
        total_inventario += valor_total
        
        worksheet.write(fila, 0, producto['id'])
        worksheet.write(fila, 1, producto['nombre'])
        worksheet.write(fila, 2, float(producto['precio_unitario']))
        worksheet.write(fila, 3, int(producto['cantidad']))
        worksheet.write(fila, 4, producto['categoria_nombre'] or 'Sin categoría')
        worksheet.write(fila, 5, valor_total)
        fila += 1

    # Total
    worksheet.write(fila + 1, 4, 'TOTAL:', cabecera_formato)
    worksheet.write(fila + 1, 5, total_inventario)

    workbook.close()
    cur.close()
    conn.close()

    return FileResponse(
        path=excel_file, 
        filename=os.path.basename(excel_file), 
        media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )