# Archivo etl.py: Solución de ETL para el proceso de compras y proveedores.

import pandas as pd

# Cargar los archivos de datos
invoice_header = pd.read_csv("Data/Invoice_header.csv")
invoice_products = pd.read_csv("Data/Invoice_products.csv")
products = pd.read_csv("Data/Products.csv")
suppliers = pd.read_csv("Data/Suppliers.csv")
daily_currencies = pd.read_csv("Data/Daily_currencies.csv")

# Ejemplo de transformación de datos (conversión a euros)
invoice_header = invoice_header.merge(daily_currencies, left_on=['fecha_factura', 'moneda'], right_on=['fecha', 'moneda'], how='left')
invoice_header['importe_en_euros'] = invoice_header['importe_factura'] * invoice_header['tipo_cambio']

# Guardar los resultados
invoice_header.to_csv("Data/transformed_invoice_header.csv", index=False)
