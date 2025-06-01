# 4. Merge Sort (Ordenação por Intercalação)
# Vantagens: Complexidade O(n log n), estável.
# Desvantagens: Usa memória adicional (O(n)).
lista = [5,2,4,3,1]
def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado
lista_ordenada = merge_sort(lista)
print(lista_ordenada)
