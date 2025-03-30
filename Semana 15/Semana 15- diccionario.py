# Crear un diccionario con información ficticia
información_personal = {
    "nombre": "Carla Morocho",
    "edad": 49,
    "ciudad": "Guayaquil",
    "profesión": "Maestra"
}

# Acceder y modificar el valor de "ciudad"
información_personal["ciudad"] = "Guayaquil"

# Agregar una nueva clave-valor "profesión"
información_personal["profesión"] = "Parbularia"

# Verificar si la clave "teléfono" existente y agregarla si no está presente
if "teléfono" not in información_personal:
    información_personal["teléfono"] = "0986640033"

# Eliminar la clave "edad"
del información_personal["edad"]

# Imprimir el diccionario final
print(información_personal)
