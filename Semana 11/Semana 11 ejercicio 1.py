Def buscar_valor(matriz, valor):
 for i in range(1en(matriz)):
  for j in range(1en(matriz[i])):
      if matriz[i] [j] == valor:
          return i, j
      return None

  matriz = [
  [10, 20, 30],
  [40, 50, 60],
  [70, 80, 90]
  ]

  valor_buscando = int(input("Ingresar el valor a buscar: "))
  