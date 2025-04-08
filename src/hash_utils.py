"""
Módulo de funciones hash y comparación de documentos.
Incluye una función hash personalizada y el cálculo de la similitud de Jaccard.
"""

def simple_hash(s):
    """
    Función hash personalizada simple para convertir un n-grama en un entero de 32 bits.
    """
    hash_val = 0
    for char in s:
        hash_val = (hash_val << 5) - hash_val + ord(char)
        hash_val &= 0xFFFFFFFF  # Limitar a 32 bits
    return hash_val

def create_hash_tables(documents_data):
    """
    Para cada documento, crea una tabla hash (un conjunto) de sus n-gramas usando simple_hash.
    Retorna un diccionario: { 'archivo.txt': conjunto(hash de cada n-grama), ... }
    """
    hash_tables = {}
    for filename, data in documents_data.items():
        hash_set = {simple_hash(ngram) for ngram in data['ngrams']}
        hash_tables[filename] = hash_set
    return hash_tables

def jaccard_similarity(set_a, set_b):
    """
    Calcula la similitud de Jaccard entre dos conjuntos.
    """
    if not set_a and not set_b:
        return 0.0
    intersection = set_a.intersection(set_b)
    union = set_a.union(set_b)
    return len(intersection) / len(union)

def compare_documents(hash_tables):
    """
    Compara cada par de documentos y calcula la similitud de Jaccard.
    Retorna una lista de diccionarios con el formato:
      { 'fileA': 'archivo1.txt', 'fileB': 'archivo2.txt', 'similarity': valor }
    """
    results = []
    filenames = list(hash_tables.keys())
    for i in range(len(filenames)):
        for j in range(i+1, len(filenames)):
            file_a = filenames[i]
            file_b = filenames[j]
            similarity = jaccard_similarity(hash_tables[file_a], hash_tables[file_b])
            results.append({
                'fileA': file_a,
                'fileB': file_b,
                'similarity': similarity
            })
    return results
