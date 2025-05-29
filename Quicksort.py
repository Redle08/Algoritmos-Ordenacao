# 5. Quick Sort (Ordenação Rápida)
# Vantagens: Muito eficiente na prática (O(n log n) em média).
# Desvantagens: Pode ter pior caso O(n^2), não é estável.
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[0]
    menores = [x for x in lista[1:] if x <= pivo]
    maiores = [x for x in lista[1:] if x > pivo]
    return quick_sort(menores) + [pivo] + quick_sort(maiores)
