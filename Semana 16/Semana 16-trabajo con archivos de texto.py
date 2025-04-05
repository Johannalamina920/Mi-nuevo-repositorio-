# Estructura de archivo de texto
# Abrimos el archivo 'my_note.txt' en modo escritura ("w")
with open("my_note.txt", "w") as file:
    # Escribimos tres líneas de notas personales
    file.write("Hoy aprendí cómo trabajar con archivos en Python.\n")
    file.write("También practiqué cómo escribir y leer archivos de texto.\n")
    file.write("Voy a subir este código a mi repositorio de Github.\n")

# Lectura de archivo de texto
# Abrimos el archivo en modo lectura ("r")
with open("my_note.txt", "r") as file:
    # Leemos todas las líneas del archivo
    lineas = file.readlines()
    # Mostramos cada línea sin saltos de línea extras
    for linea in lineas:
        print(linea.strip())

# El uso de "with" cierra automáticamente el archivo después de cada bloque