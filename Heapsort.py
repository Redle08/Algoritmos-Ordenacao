# 6. Heap Sort
# Vantagens: Complexidade O(n log n), não usa memória extra.
# Desvantagens: Não é estável, implementação mais complexa.
lista = [5,2,4,3,1]
import heapq

def heap_sort(lista):
    heapq.heapify(lista)
    return [heapq.heappop(lista) for _ in range(len(lista))]

lista_ordenada = heap_sort(lista)
print(lista_ordenada)
