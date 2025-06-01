# 3. Insertion Sort (Ordenação por Inserção)
# Vantagens: Eficiente para listas pequenas ou quase ordenadas.
# Desvantagens: Ineficiente para listas grandes (O(n²)).
lista = [5,2,4,3,1]
def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista
lista_ordenada = insertion_sort(lista)
print(lista_ordenada)
