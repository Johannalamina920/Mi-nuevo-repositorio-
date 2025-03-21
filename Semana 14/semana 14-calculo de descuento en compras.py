# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Programa principal
def main():
    # Primera llamada solo con el monto, usa el porcentaje por defecto (10%):
    monto_compra1 = 150.00
    descuento1 = calcular_descuento(monto_compra1)
    monto_final1 = monto_compra1 - descuento1

    print(f"Compra 1 :")
    print(f"Monto total de la compra: ${monto_compra1:.2f}")
    print(f"Descuento aplicado (por defecto 10%): ${descuento1:.2f}")
    print(f"Monto final a pagar: ${monto_final1:.2f}")
    print(f"_" * 40)

    # Segunda llamada con monto y porcentaje de descuento personalizado
    monto_compra2 = 250.00
    porcentaje_descuento_personalizado = 15
    descuento2 = calcular_descuento(monto_compra2, porcentaje_descuento_personalizado)
    monto_final2 = monto_compra2 - descuento2

    print(f"Compra 2 :")
    print(f"Monto total de la compra: ${monto_compra2:.2f}")
    print(f"Descuento aplicado ({porcentaje_descuento_personalizado}%): ${descuento2:.2f}")
    print(f"Monto final a pagar: ${monto_final2:.2f}")

# Ejecutar el programa
if __name__ == "__main__":
    main()