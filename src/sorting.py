"""
Módulo de ordenamiento y visualización de resultados.
Incluye la implementación de Merge Sort para ordenar los pares de documentos según su similitud.
"""

def merge_sort(arr):
    """
    Ordena una lista de diccionarios (con la clave 'similarity') en orden descendente.
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i]['similarity'] >= right[j]['similarity']:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def show_top_results(results, top_n):
    """
    Muestra en consola los top N pares de documentos con mayor similitud.
    """
    print(f'\nTop {top_n} documentos más similares:')
    top_results = results[:top_n]
    for res in top_results:
        print(f"{res['fileA']} <--> {res['fileB']} | Similitud: {res['similarity']:.4f}")
