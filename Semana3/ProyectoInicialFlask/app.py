from flask import Flask, render_template, request, send_file, redirect, url_for, flash
import pandas as pd
import os
from werkzeug.utils import secure_filename
import uuid

app = Flask(__name__)
app.secret_key = "inventario_secreto_2025"
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['DOWNLOAD_FOLDER'] = 'downloads'

# Crear carpetas si no existen
for folder in [app.config['UPLOAD_FOLDER'], app.config['DOWNLOAD_FOLDER']]:
    if not os.path.exists(folder):
        os.makedirs(folder)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procesar', methods=['POST'])
def procesar_archivo():
    # Verificar si se subió un archivo
    if 'archivo' not in request.files:
        flash('No se seleccionó ningún archivo', 'error')
        return redirect(url_for('index'))
    
    archivo = request.files['archivo']
    
    # Verificar si el nombre del archivo está vacío
    if archivo.filename == '':
        flash('No se seleccionó ningún archivo', 'error')
        return redirect(url_for('index'))

    # Generar nombre único para el archivo
    filename = secure_filename(archivo.filename)
    extension = os.path.splitext(filename)[1]
    
    if extension.lower() not in ['.xlsx', '.xls']:
        flash('Solo se permiten archivos Excel (.xlsx, .xls)', 'error')
        return redirect(url_for('index'))
    
    # Generar ID único para este procesamiento
    proceso_id = str(uuid.uuid4())
    
    # Guardar el archivo
    ruta_archivo = os.path.join(app.config['UPLOAD_FOLDER'], f"{proceso_id}{extension}")
    archivo.save(ruta_archivo)
    
    try:
        # Leer el archivo de Excel
        df = pd.read_excel(ruta_archivo)
        
        # Verificar que el Excel tenga las columnas necesarias
        required_columns = ['Producto', 'Cantidad', 'Precio Unitario']
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            flash(f'El archivo no contiene las columnas requeridas: {", ".join(missing_columns)}', 'error')
            os.remove(ruta_archivo)  # Eliminar el archivo subido
            return redirect(url_for('index'))
        
        # Procesar datos
        df['Valor Total'] = df['Cantidad'] * df['Precio Unitario']
        valor_inventario_total = df['Valor Total'].sum()
        
        # Crear resumen
        resumen = pd.DataFrame({
            'Producto': ['TOTAL INVENTARIO'],
            'Cantidad': [''],
            'Precio Unitario': [''],
            'Valor Total': [valor_inventario_total]
        })
        
        # Concatenar el DataFrame original con el resumen
        df_final = pd.concat([df, resumen], ignore_index=True)
        
        # Generar archivo de salida
        archivo_salida = os.path.join(app.config['DOWNLOAD_FOLDER'], f"informe_inventario_{proceso_id}.xlsx")
        df_final.to_excel(archivo_salida, index=False)
        
        # Estadísticas para mostrar
        stats = {
            'total_productos': len(df),
            'valor_total': f"${valor_inventario_total:,.2f}",
            'producto_mas_caro': df.loc[df['Precio Unitario'].idxmax()]['Producto'],
            'producto_mas_cantidad': df.loc[df['Cantidad'].idxmax()]['Producto']
        }
        
        # Eliminar archivo original subido
        os.remove(ruta_archivo)
        
        return render_template('resultado.html', 
                               archivo_salida=f"informe_inventario_{proceso_id}.xlsx",
                               stats=stats)
        
    except Exception as e:
        # En caso de error, eliminar cualquier archivo temporal
        if os.path.exists(ruta_archivo):
            os.remove(ruta_archivo)
        flash(f'Error al procesar el archivo: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/descargar/<filename>')
def descargar_archivo(filename):
    return send_file(os.path.join(app.config['DOWNLOAD_FOLDER'], filename),
                     as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
