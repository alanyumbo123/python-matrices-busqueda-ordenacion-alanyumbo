# Programa 2: Ordenación de una fila de una matriz 3x3
# Autor: Alan

MATRIZ = [
    [9, 4, 7],
    [8, 5, 2],
    [6, 3, 1]
]

def bubble_sort(lista):
    a = lista[:]
    n = len(a)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def ordenar_fila(matriz, indice_fila):
    nueva = [fila[:] for fila in matriz]
    nueva[indice_fila] = bubble_sort(nueva[indice_fila])
    return nueva

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

print("Matriz original:")
mostrar_matriz(MATRIZ)

indice = int(input("¿Qué fila quieres ordenar? (0, 1 o 2): "))
ordenada = ordenar_fila(MATRIZ, indice)

print("\nMatriz resultante:")
mostrar_matriz(ordenada)
