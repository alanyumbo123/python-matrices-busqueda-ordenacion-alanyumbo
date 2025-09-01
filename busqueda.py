# Programa 1: Búsqueda en matriz 3x3
# Autor: Alan

MATRIZ = [
    [4, 7, 9],
    [2, 5, 8],
    [1, 3, 6]
]

def buscar_valor(matriz, objetivo):
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor == objetivo:
                return i, j
    return None

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

print("Matriz:")
mostrar_matriz(MATRIZ)
objetivo = int(input("Ingresa el número que quieres buscar: "))

pos = buscar_valor(MATRIZ, objetivo)
if pos is None:
    print(f"No se encontró {objetivo} en la matriz.")
else:
    i, j = pos
    print(f"Encontrado: {objetivo} en la posición (fila={i}, columna={j}).")
