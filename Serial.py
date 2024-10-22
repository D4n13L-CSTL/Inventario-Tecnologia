import barcode
from barcode.writer import ImageWriter

# Define el tipo de código de barras (en este caso, Code 128)
code128 = barcode.get_barcode_class('code128')

# Genera el código de barras con el valor serial deseado
codigo_serial = code128('sssds5', writer=ImageWriter())

# Guarda el código de barras como una imagen en formato PNG
filename = codigo_serial.save('codigo_serial')

# Imprime el valor del código de barras
print(f"Código de barras generado: {codigo_serial.get_fullcode()}")
