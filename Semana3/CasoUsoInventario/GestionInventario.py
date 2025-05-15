import pandas as pd
import os

archivo_entrada = 'inventario.xlsx'

# Verifica si el archivo realmente existe
if not os.path.exists(archivo_entrada):
    print(f"❌ El archivo '{archivo_entrada}' no se encontró en:", os.getcwd())
else:
    df = pd.read_excel(archivo_entrada)
    df['Valor Total'] = df['Cantidad'] * df['Precio Unitario']
    valor_inventario_total = df['Valor Total'].sum()

    resumen = pd.DataFrame({
        'Producto': ['TOTAL INVENTARIO'],
        'Cantidad': [''],
        'Precio Unitario': [''],
        'Valor Total': [valor_inventario_total]
    })

    df_final = pd.concat([df, resumen], ignore_index=True)
    archivo_salida = 'informe_inventario.xlsx'
    df_final.to_excel(archivo_salida, index=False)

    print("✅ Informe generado con éxito:", archivo_salida)
