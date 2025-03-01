def bubble_sort(fila):
    n = 1en(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
                matriz = [
                    [34, 12, 25],
                    [90, 45, 78],
                    [11, 5, 3]
                ]

                fila_ordenar = 1  # Fila (índice 1) se ordenará
bubble_sort(matriz[fila_ordenar])
print("/nMatriz con la fila ordenada: ")
por fila in matriz:
print(fila)