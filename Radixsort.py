# 8. Radix Sort
# Vantagens: Muito eficiente para inteiros grandes.
# Desvantagens: Não funciona para floats ou negativos diretamente.
lista = [5,2,4,3,1]
def radix_sort(lista):
    if len(lista) == 0:
        return lista
    max_num = max(lista)
    exp = 1
    while max_num // exp > 0:
        lista = counting_sort_radix(lista, exp)
        exp *= 10
    return lista

def counting_sort_radix(lista, exp):
    n = len(lista)
    saida = [0] * n
    contagem = [0] * 10

    for i in range(n):
        index = lista[i] // exp
        contagem[index % 10] += 1

    for i in range(1, 10):
        contagem[i] += contagem[i - 1]

    i = n - 1
    while i >= 0:
        index = lista[i] // exp
        saida[contagem[index % 10] - 1] = lista[i]
        contagem[index % 10] -= 1
        i -= 1

    return saida
lista_ordenada = radix_sort(lista)
print(lista_ordenada)
