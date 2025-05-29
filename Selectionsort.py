# 1. Selection Sort (Ordenação por Seleção)
# Vantagens: Simples de implementar, não requer memória adicional.
# Desvantagens: Ineficiente para listas grandes (complexidade O(n²)).

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    return lista


