# 9. Bucket Sort
# Vantagens: Muito eficiente para dados uniformemente distribuídos.
# Desvantagens: Não é bom para dados não uniformes ou com muitos valores repetidos.


def bucket_sort(lista):
    if not lista:
      return lista

    num_buckets = len(lista)
    buckets = [[] for _ in range(num_buckets)]

    max_val = max(lista)
    for num in lista:
        index = min(int(num * num_buckets / (max_val+1)), num_buckets-1)
        buckets[index].append(num)

    for bucket in buckets:
      bucket.sort()

    sorted_lista = []
    for bucket in buckets:
        sorted_lista.extend(bucket)

    return sorted_lista

