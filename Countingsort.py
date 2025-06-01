# 7. Counting Sort
# Vantagens: Muito rápido para números inteiros pequenos.
# Desvantagens: Ineficiente com intervalos grandes ou dados não inteiros.

lista = [5, 2, 4, 3, 1]

def counting_sort(lista):
    if not lista:
        return lista
    max_val = max(lista)
    min_val = min(lista)
    tamanho = max_val - min_val + 1
    contagem = [0] * tamanho

    for num in lista:
        contagem[num - min_val] += 1

    resultado = []
    for i, c in enumerate(contagem):
        resultado.extend([i + min_val] * c)
    return resultado

lista_ordenada = counting_sort(lista)
print(lista_ordenada)
