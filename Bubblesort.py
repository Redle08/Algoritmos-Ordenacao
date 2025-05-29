# 2. Bubble Sort (Ordenação por Bolha)
# Vantagens: Fácil de entender e implementar.
# Desvantagens: Muito ineficiente para listas grandes (O(n²)).

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
